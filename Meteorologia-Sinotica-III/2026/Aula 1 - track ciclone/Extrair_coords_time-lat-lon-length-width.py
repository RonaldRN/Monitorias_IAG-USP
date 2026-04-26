import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import argparse
from matplotlib.widgets import RectangleSelector
from matplotlib.patches import Rectangle
import shapefile
import os

# ==========================================================
# Configurações
# ==========================================================
parser = argparse.ArgumentParser(
    description="Extrair centro e dimensões de ciclones a partir de NetCDF"
)

parser.add_argument(
    "file_nc",
    type=str,
    help="Caminho do arquivo NetCDF"
)

parser.add_argument(
    "--var",
    type=str,
    default="msl",
    help="Nome da variável no NetCDF. Default: msl"
)

parser.add_argument(
    "--level",
    type=float,
    default=None,
    help="Nível isobárico a selecionar, se existir dimensão vertical. Exemplo: --level 850"
)

parser.add_argument(
    "--out",
    type=str,
    default="track_ciclone.txt",
    help="Nome do arquivo de saída (default: track_ciclone.txt)"
)

parser.add_argument("--shp", type=str, default=None,
                    help="Shapefile de continentes (opcional)")

args = parser.parse_args()

file_nc = args.file_nc
outfile = args.out
varname = args.var
level_value = args.level
shp_path = args.shp

if not os.path.exists(file_nc):
    raise FileNotFoundError(f"Arquivo não encontrado: {file_nc}")

if shp_path and not os.path.exists(shp_path):
    raise FileNotFoundError(f"Shapefile não encontrado: {shp_path}")

# ==========================================================
# Abrir dataset
# ==========================================================
ds = xr.open_dataset(file_nc)

# ==========================================================
# Selecionar nível isobárico, se solicitado
# ==========================================================
if level_value is not None:
    possible_level_names = [
        "level",
        "pressure_level",
        "isobaricInhPa",
        "plev",
        "lev"
    ]

    level_name = None

    for name in possible_level_names:
        if name in ds.coords or name in ds.dims:
            level_name = name
            break

    if level_name is None:
        raise ValueError(
            "Você passou --level, mas não encontrei uma dimensão/coordenada "
            "de nível isobárico no NetCDF."
        )

    ds = ds.sel({level_name: level_value}, method="nearest")

    print(f"Nível selecionado: {level_name} = {float(ds[level_name].values)}")
    
# ==========================================================
# Detectar coordenadas automaticamente
# ==========================================================
lat_name = None
lon_name = None
time_name = None

for name in ds.coords:
    lname = name.lower()
    if lname in ["lat", "latitude"]:
        lat_name = name
    elif lname in ["lon", "longitude"]:
        lon_name = name
    elif lname in ["time", "valid_time", "date"]:
        time_name = name

if lat_name is None or lon_name is None or time_name is None:
    raise ValueError("Não consegui detectar lat/lon/time no NetCDF.")

lat_min = float(ds[lat_name].min())
lat_max = float(ds[lat_name].max())
lon_min = float(ds[lon_name].min())
lon_max = float(ds[lon_name].max())

# DETECTAR FORMATO DE LONGITUDE
use_lon_360 = lon_max > 180
print(f"Formato de longitude detectado: {'0-360' if use_lon_360 else '-180 +180'}")

# ==========================================================
# FUNÇÃO SHAPEFILE
# ==========================================================
def plot_shapefile(ax, shp_path, use_lon_360,
                   edgecolor="black",
                   linewidth=0.6
                   ):

    sf = shapefile.Reader(shp_path)

    for shp in sf.shapes():
        pts = np.array(shp.points)
        if pts.size == 0:
            continue

        x = pts[:, 0]
        y = pts[:, 1]

        if use_lon_360:
            x = np.where(x < 0, x + 360, x)
        else:
            x = np.where(x > 180, x - 360, x)

        parts = list(shp.parts) + [len(pts)]

        for i in range(len(parts) - 1):
            xs = x[parts[i]:parts[i+1]]
            ys = y[parts[i]:parts[i+1]]

            # QUEBRAR NO DATELINE
            jumps = np.abs(np.diff(xs)) > 180

            start = 0

            for j, jump in enumerate(jumps):
                if jump:
                    ax.plot(xs[start:j+1], ys[start:j+1], 
                            color=edgecolor, linewidth=linewidth)
                    start = j + 1
            
            ax.plot(xs[start:], ys[start:], color=edgecolor, linewidth=linewidth)

# ==========================================================
# Criar arquivo de saída no padrão:
# time;Lat;Lon,length;width
# ==========================================================
nt = len(ds[time_name])
da_all = ds[varname]

with open(outfile, "w") as f:
    f.write("time;Lat;Lon;length;width\n")

# ==========================================================
# Loop temporal
# ==========================================================
for n in range(nt):

    da = da_all.isel({time_name: n})

    # Converter Pa -> hPa se necessário
    if float(da.mean()) > 2000:
        da_plot = da / 100.0
    else:
        da_plot = da

    time_value = pd.to_datetime(ds[time_name].isel({time_name: n}).values)
    time_txt = time_value.strftime("%Y-%m-%d-%H%M")
    time_title = time_value.strftime("%HZ%d%b%Y").upper()

    # ======================================================
    # Plot simples com Matplotlib
    # ======================================================
    fig, ax = plt.subplots(figsize=(7, 9))
        
    vmin = np.floor(float(da_plot.min()))
    vmax = np.ceil(float(da_plot.max()))
    levels = np.arange(vmin, vmax + 4, 4)
    
    cs = ax.contour(
        ds[lon_name].values,
        ds[lat_name].values,
        da_plot.values,
        levels=levels,
        colors="black",
        linewidths=1
    )

    ax.clabel(cs, inline=True, fontsize=8, fmt="%.0f")

    ax.set_xlim(lon_min, lon_max)
    ax.set_ylim(lat_min, lat_max)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_title(f"Mean sea level pressure {time_title}", fontsize=14)

    ax.grid(True, linestyle="--", alpha=0.4)

    # SHAPEFILE
    if shp_path is not None:
        plot_shapefile(
            ax, 
            shp_path, 
            use_lon_360, 
            facecolor=None,  
            edgecolor="red", 
            linewidth=1.5,
            alpha=1.0,
            label="Continent"
            )
    ax.legend(loc="upper right")

    print("\n======================================")
    print(f"Tempo {n+1}/{nt}: {time_txt}")
    print("Clique com o botão esquerdo, arraste a caixa e solte.")
    print("Feche a janela se quiser pular este tempo.")
    print("======================================")

    selection = {}

    def onselect(eclick, erelease):
        lon_a, lat_a = eclick.xdata, eclick.ydata
        lon_b, lat_b = erelease.xdata, erelease.ydata

        if lon_a is None or lon_b is None or lat_a is None or lat_b is None:
            return

        lon_left = min(lon_a, lon_b)
        lon_right = max(lon_a, lon_b)
        lat_bottom = min(lat_a, lat_b)
        lat_top = max(lat_a, lat_b)

        selection["lon_left"] = lon_left
        selection["lon_right"] = lon_right
        selection["lat_bottom"] = lat_bottom
        selection["lat_top"] = lat_top

        plt.close(fig)

    selector = RectangleSelector(
        ax,
        onselect,
        useblit=True,
        button=[1],
        minspanx=0.1,
        minspany=0.1,
        spancoords="data",
        interactive=True
    )

    plt.show()

    if not selection:
        print("Nenhuma caixa selecionada. Pulando este tempo.")
        plt.close(fig)
        continue

    lon_left = selection["lon_left"]
    lon_right = selection["lon_right"]
    lat_bottom = selection["lat_bottom"]
    lat_top = selection["lat_top"]

    lon_center = (lon_left + lon_right) / 2.0
    lat_center = (lat_bottom + lat_top) / 2.0

    length = lon_right - lon_left
    width = lat_top - lat_bottom

    with open(outfile, "a") as f:
        f.write(
            f"{time_txt};"
            f"{lat_center:.4f};"
            f"{lon_center:.4f};"
            f"{length:.4f};"
            f"{width:.4f}\n"
        )

    print(
        f"Salvo: {time_txt};"
        f"{lat_center:.4f};"
        f"{lon_center:.4f};"
        f"{length:.4f};"
        f"{width:.4f}"
    )

print("\nProcessamento finalizado.")
print(f"Arquivo salvo: {outfile}")