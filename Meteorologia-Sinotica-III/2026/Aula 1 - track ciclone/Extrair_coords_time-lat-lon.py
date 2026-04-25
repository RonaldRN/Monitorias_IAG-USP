import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.widgets import RectangleSelector
from matplotlib.patches import Rectangle

# ==========================================================
# Configurações
# ==========================================================
file_nc = "/home/ronaldrn/GrADS_scripts/equipe3_mslp.nc"
outfile = "track_ciclone_equipe3.txt"
varname = "msl"

# ==========================================================
# Abrir dataset
# ==========================================================
ds = xr.open_dataset(file_nc)

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

nt = len(ds[time_name])
da_all = ds[varname]

# ==========================================================
# Criar arquivo de saída no padrão:
# time;Lat;Lon
# ==========================================================
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