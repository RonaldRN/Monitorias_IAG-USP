# 🌎 Meteorologia Sinótica II — IAG/USP

Materiais computacionais de apoio à disciplina **Meteorologia Sinótica II (ACA0523)** do Instituto de Astronomia, Geofísica e Ciências Atmosféricas da Universidade de São Paulo (**IAG-USP**), desenvolvidos no contexto do **Programa de Aperfeiçoamento de Ensino (PAE)**.

O objetivo é aproximar os conceitos de meteorologia sinótica de **dados atmosféricos reais** mediante a elaboração de cartas, diagnósticos dinâmicos e termodinâmicos, representações tridimensionais e cortes verticais interativos em Python.

> **Material didático complementar:** os notebooks não substituem as aulas nem a bibliografia oficial da disciplina. Foram desenvolvidos principalmente para o **Google Colab**, embora também possam ser executados em ambientes Jupyter locais, com as dependências apropriadas.

## 👨‍💻 Monitor PAE

**Ronald Guiuseppi Ramírez Nina**  
Doutorando em Ciências Atmosféricas — IAG-USP  
Monitor/Estagiário PAE — Meteorologia Sinótica II

**Contato:** [ronald.ramirez.nina@usp.br](mailto:ronald.ramirez.nina@usp.br) · [ronald.ramirez.nina@alumni.usp.br](mailto:ronald.ramirez.nina@alumni.usp.br) · [ronald.ramirez.nina@gmail.com](mailto:ronald.ramirez.nina@gmail.com)  
**GitHub:** [@RonaldRN](https://github.com/RonaldRN)

## 📂 Notebooks e códigos

| Arquivo | Conteúdo principal |
|---|---|
| [`Isentropic_charts_GFS_analysis.ipynb`](Isentropic_charts_GFS_analysis.ipynb) | Cartas isentrópicas do GFS em **310, 330 e 350 K**, com pressão, vento e vorticidade potencial; diagnóstico de esteiras transportadoras (*conveyor belts*). |
| [`JET_POLAR_SUBTROPICAL.ipynb`](JET_POLAR_SUBTROPICAL.ipynb) | Identificação dos **jatos subtropical e polar**, mapas em níveis superiores e cortes verticais de longitude/latitude constantes e interativos A–B. |
| [`IDENTIFICATION_SALLJ.ipynb`](IDENTIFICATION_SALLJ.ipynb) | **Jato de Baixos Níveis da América do Sul (SALLJ)**: critérios em 850–700 hPa, circulação em 250 hPa, campos termodinâmicos, transporte/convergência de umidade e cortes verticais com representação da topografia dos Andes. **Adicionar este notebook ao repositório com esse nome para ativar o link.** |
| [`Synoptic_chart_Reanalysis_ERA5.ipynb`](Synoptic_chart_Reanalysis_ERA5.ipynb) | Cartas sinóticas elaboradas com a reanálise **ERA5**. |
| [`Synoptic_charts_GFS_analysis_Part_I.ipynb`](Synoptic_charts_GFS_analysis_Part_I.ipynb) | Cartas sinóticas e campos meteorológicos da análise **GFS — Parte I**. |
| [`Synoptic_charts_GFS_analysis_Part_II.ipynb`](Synoptic_charts_GFS_analysis_Part_II.ipynb) | Diagnósticos complementares **GFS — Parte II**, com apresentação inspirada nas cartas do *GFS Archive* de Alicia M. Bentley. |
| [`Synoptic_charts_identification_High_Low_pressure_systems_GFS_analysis.ipynb`](Synoptic_charts_identification_High_Low_pressure_systems_GFS_analysis.ipynb) | Análise interativa da **estrutura vertical de altas e baixas pressões** com PRNMM e altura geopotencial em 850, 700 e 500 hPa, usando Plotly/Dash. |
| [`ZCIT_GOES19_GFS.ipynb`](ZCIT_GOES19_GFS.ipynb) | Análise da **Zona de Convergência Intertropical (ZCIT)** combinando imagens **GOES-19** e campos **GFS**. |
| [`utilities_new_version.py`](utilities_new_version.py) | Rotinas auxiliares, inclusive acesso/processamento de dados GOES-19, coordenadas e reprojeções. |

> **Nota sobre o SALLJ:** a descrição acima foi preparada com base no notebook `IDENTIFICATION_SALLJ(2).ipynb` trabalhado durante a atualização. O nome `IDENTIFICATION_SALLJ.ipynb` é o nome de publicação sugerido; confirme-o na pasta antes de publicar este README.

## 🧭 Principais atividades

### Cartas sinóticas do GFS e ERA5

Construção de mapas em diferentes níveis isobáricos para avaliar a circulação atmosférica, os sistemas de pressão e a organização de campos dinâmicos e termodinâmicos. As **Partes I e II do GFS** complementam as atividades de cartas sinóticas e exploram diferentes combinações de variáveis.

### 🌡️ Superfícies isentrópicas

O notebook de análise isentrópica calcula temperatura potencial e vorticidade potencial baroclínica (em **PVU**) e interpola pressão, vento e vorticidade potencial sobre as superfícies de **310, 330 e 350 K**. Também permite explorar estruturas associadas ao transporte atmosférico e às esteiras transportadoras.

### 🌀 Altas e baixas pressões: estrutura vertical

A análise com **Plotly e Dash** utiliza a pressão reduzida ao nível médio do mar e as alturas geopotenciais em **850, 700 e 500 hPa**. O usuário delimita um sistema no mapa de superfície e visualiza o mesmo recorte nos níveis superiores, auxiliando a discussão de alinhamento vertical, inclinação e estrutura térmica dos sistemas.

A identificação de **núcleo quente ou frio** deve ser interpretada juntamente com os campos de temperatura e espessura; apenas a variação da amplitude das isolinhas de geopotencial não constitui, por si só, uma confirmação termodinâmica definitiva.

### 🌬️ Jatos subtropical e polar

Os produtos em altos níveis incluem intensidade do vento, altura geopotencial, temperatura potencial e vorticidade potencial, além de cortes verticais fixos e **interativos A–B** para investigar a estrutura vertical e a posição da tropopausa dinâmica.

### 🌎 Jato de Baixos Níveis da América do Sul (SALLJ)

O notebook do SALLJ utiliza o **GFS** para examinar a circulação de baixos níveis a leste dos Andes. Os mapas combinam:

- **Vento em 850 hPa:** isotacas a partir de **12 m s⁻¹** e vetores horizontais;
- **Cisalhamento vetorial 850–700 hPa:** isolinhas a partir de **6 m s⁻¹** nas regiões de vento intenso;
- **Espessura geopotencial 850–500 hPa:** isolinhas em decâmetros (**dam**);
- **Temperatura potencial equivalente em 850 hPa:** isolinhas de **θe** em kelvin (**K**);
- **Convergência horizontal de umidade em 850 hPa:** valores positivos de **−∇ₕ·(qVₕ)**, apresentados em **10⁻⁵ s⁻¹**;
- **Circulação em 250 hPa:** intensidade do vento e linhas de corrente, para contextualização dos sistemas de altos níveis.

São produzidos **cortes verticais em longitude constante, latitude constante e sobre um transecto interativo A–B**. No modo interativo, o estudante seleciona os pontos A e B no mapa e utiliza o botão **“Gerar corte A-B”** para visualizar o perfil correspondente.

Nos cortes, a **pressão de superfície** do GFS (`sp_hpa`) permite representar a barreira orográfica dos **Andes** no eixo vertical em hPa e ocultar os campos isobáricos abaixo do terreno. O fluxo meridional de umidade (**qv**) e a convergência horizontal complementam a análise do transporte de umidade.

> **Interpretação dos critérios:** velocidade ≥ 12 m s⁻¹ e cisalhamento ≥ 6 m s⁻¹ indicam regiões candidatas ao jato, mas não substituem a verificação do perfil vertical do vento, da direção do escoamento e do enfraquecimento acima do núcleo de baixos níveis. O cisalhamento vetorial não equivale necessariamente à diminuição da velocidade.

### 🛰️ ZCIT com GOES-19 e GFS

Integra imagens de satélite e campos de análise atmosférica para estudar a organização da nebulosidade e da circulação associada à **Zona de Convergência Intertropical**.

## ▶️ Como executar

### Opção A — Google Colab

1. Abra o notebook desejado no GitHub e utilize a opção de abri-lo no Colab, ou carregue o arquivo `.ipynb` no [Google Colab](https://colab.research.google.com/).
2. Execute primeiro as células de preparação do ambiente e instalação das bibliotecas solicitadas no notebook.
3. Configure a **data, horário, ciclo/tempo de previsão, região e diretórios de entrada/saída**.
4. Execute as células sequencialmente, garantindo que os arquivos meteorológicos necessários tenham sido obtidos.
5. Nos notebooks interativos, habilite o backend/widget solicitado antes de criar o mapa e mantenha ferramentas de zoom/pan desativadas ao selecionar pontos com o mouse.

> Alguns notebooks utilizam caminhos do Google Drive, shapefiles e dados externos. Ajuste esses caminhos ao seu ambiente antes de executar. A disponibilidade de dados depende do produto e da data escolhidos.

### Opção B — Execução local

```bash
git clone https://github.com/RonaldRN/Monitorias_IAG-USP.git
cd Monitorias_IAG-USP/Meteorologia-Sinotica-II
jupyter lab
```

Também é possível utilizar Jupyter Notebook ou VS Code com suporte a notebooks.

### Atualizar uma cópia clonada

Na raiz do repositório:

```bash
git pull origin main
```

Para baixar sem Git, use **Code → Download ZIP** na [página do repositório](https://github.com/RonaldRN/Monitorias_IAG-USP).

## 🐍 Dependências e ambiente

As bibliotecas variam entre notebooks. Entre as utilizadas estão:

```text
numpy              scipy             pandas
xarray             metpy             pint
matplotlib         cartopy           shapely
netCDF4            cfgrib            eccodes
pygrib             pyproj            regionmask
ipywidgets         ipympl            plotly
dash               kaleido           requests
boto3              cmocean           GDAL
```

**Recomendações:**

- Instale apenas os pacotes exigidos pelo notebook escolhido, preferencialmente seguindo suas células iniciais.
- Para ler arquivos **GFS GRIB2**, `cfgrib` depende do **ecCodes**; algumas instalações de `pygrib`, `GDAL` e Cartopy exigem bibliotecas nativas.
- Verifique cuidadosamente as unidades ao combinar **Xarray, MetPy e Pint**, especialmente em diagnósticos de fluxo e convergência de umidade.
- A interação com o mouse no Google Colab pode requerer `ipympl`, `ipywidgets` e o gerenciador de widgets do Colab habilitado.
- A exportação estática de gráficos Plotly pode exigir `kaleido`.

## 🗂️ Dados meteorológicos

| Fonte | Utilização |
|---|---|
| **GFS — Global Forecast System (NOAA/NCEP)** | Campos em níveis isobáricos e superfície, identificação de jatos, sistemas de pressão, termodinâmica e cortes verticais. |
| **ERA5 — ECMWF Reanalysis v5** | Construção de cartas e diagnósticos sinóticos com dados de reanálise. |
| **GOES-19** | Imagens de satélite para análise de nebulosidade e ZCIT; determinadas rotinas obtêm dados de serviços públicos na AWS. |

Nos cortes do SALLJ, a pressão de superfície **`sp_hpa`** precisa corresponder ao **mesmo ciclo e horário válido** dos campos atmosféricos e estar corretamente alinhada à grade horizontal. A PRNMM não deve ser utilizada como substituta da pressão sobre o terreno.

## 📚 Créditos e referências

**Alicia M. Bentley — GFS Archive.** A organização e o estilo de determinados diagnósticos, especialmente nas cartas isentrópicas e na Parte II do GFS, foram inspirados em produtos disponibilizados no [GFS Archive](https://www.atmos.albany.edu/student/abentley/realtime.html).

A referência constitui reconhecimento da **inspiração conceitual e visual**: os notebooks deste repositório foram desenvolvidos/adaptados para fins didáticos no âmbito da monitoria PAE e não integram o projeto original do GFS Archive.

## 🎯 Proposta pedagógica

Ao explorar os notebooks, recomenda-se observar **quais variáveis foram combinadas, em quais níveis, com quais unidades e com que interpretação física**. Os códigos são pontos de partida para investigar diferentes datas, regiões e situações sinóticas — não procedimentos automáticos de identificação validados para todas as condições meteorológicas.

---

**IAG-USP — Ciências Atmosféricas** · **Meteorologia Sinótica II (ACA0523)**  
Material de apoio desenvolvido no contexto das atividades de monitoria do **Programa de Aperfeiçoamento de Ensino (PAE)**.
