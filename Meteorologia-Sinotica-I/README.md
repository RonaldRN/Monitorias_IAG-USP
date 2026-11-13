# 🌎 Meteorologia Sinótica I — IAG/USP

**Disciplina:** Meteorologia Sinótica I (ACA0522)  
**Instituição:** Instituto de Astronomia, Geofísica e Ciências Atmosféricas — Universidade de São Paulo (IAG-USP)  
**Material:** notebooks Jupyter, rotinas Python e arquivos auxiliares para atividades práticas e monitoria

Este diretório reúne materiais computacionais de apoio à disciplina **Meteorologia Sinótica I**, desenvolvidos e organizados no contexto das atividades de monitoria e do **Programa de Aperfeiçoamento de Ensino (PAE)**. O objetivo é aproximar a teoria da prática de análise meteorológica por meio de **observações de superfície, análises de modelos numéricos, reanálises e imagens de satélite**, utilizando Python para obter, visualizar e interpretar dados atmosféricos.

> **Nota didática:** estes materiais complementam as aulas e orientações oficiais da disciplina. Serviços de dados e dependências computacionais podem mudar; consulte as primeiras células de cada notebook antes de executá-lo.

## 📑 Navegação

- [Notebooks e materiais disponíveis](#-notebooks-e-materiais-disponíveis)
- [Principais temas de aprendizagem](#-principais-temas-de-aprendizagem)
- [Execução no Google Colab](#-execução-no-google-colab)
- [Execução local e dependências](#-execução-local-e-dependências)
- [Fontes de dados e boas práticas](#-fontes-de-dados-e-boas-práticas)
- [Monitor PAE e contato](#-monitor-pae-e-contato)

## 📂 Notebooks e materiais disponíveis

A pasta contém **10 notebooks Jupyter (`.ipynb`)**, um módulo Python auxiliar, duas paletas de cores (`.cpt`) e este README. Os links abaixo apontam para os arquivos reais da pasta, verificados na branch `main`.

| Tema | Notebook | Objetivo didático | Execução |
|:--|:--|:--|:--|
| **Dados de estações do INMET** | [`Download_INMET_AWS_data.ipynb`](Download_INMET_AWS_data.ipynb) | Obtenção e exploração de dados observacionais de estações meteorológicas automáticas. | [Abrir no Colab](https://colab.research.google.com/github/RonaldRN/Monitorias_IAG-USP/blob/main/Meteorologia-Sinotica-I/Download_INMET_AWS_data.ipynb) |
| **Cartas sinóticas — GFS** | [`Synoptic_charts_GFS_analysis.ipynb`](Synoptic_charts_GFS_analysis.ipynb) | Elaboração de cartas sinóticas com campos atmosféricos do GFS. | [Abrir no Colab](https://colab.research.google.com/github/RonaldRN/Monitorias_IAG-USP/blob/main/Meteorologia-Sinotica-I/Synoptic_charts_GFS_analysis.ipynb) |
| **Cartas sinóticas — Parte I** | [`Synoptic_charts_GFS_analysis_Part-I.ipynb`](Synoptic_charts_GFS_analysis_Part-I.ipynb) | Introdução à interpretação de variáveis e campos meteorológicos do GFS. | [Abrir no Colab](https://colab.research.google.com/github/RonaldRN/Monitorias_IAG-USP/blob/main/Meteorologia-Sinotica-I/Synoptic_charts_GFS_analysis_Part-I.ipynb) |
| **Cartas sinóticas — Parte II** | [`Synoptic_charts_GFS_analysis_Part-II.ipynb`](Synoptic_charts_GFS_analysis_Part-II.ipynb) | Continuação das análises com cartas e combinações adicionais de campos atmosféricos. | [Abrir no Colab](https://colab.research.google.com/github/RonaldRN/Monitorias_IAG-USP/blob/main/Meteorologia-Sinotica-I/Synoptic_charts_GFS_analysis_Part-II.ipynb) |
| **Cartas sinóticas — ERA5** | [`Synoptic_chart_Reanalysis_ERA5.ipynb`](Synoptic_chart_Reanalysis_ERA5.ipynb) | Construção e interpretação de cartas da reanálise ERA5. | [Abrir no Colab](https://colab.research.google.com/github/RonaldRN/Monitorias_IAG-USP/blob/main/Meteorologia-Sinotica-I/Synoptic_chart_Reanalysis_ERA5.ipynb) |
| **Altas e baixas pressões** | [`Synoptic_charts_identification_High_Low_pressure_systems_GFS_analysis.ipynb`](Synoptic_charts_identification_High_Low_pressure_systems_GFS_analysis.ipynb) | Identificação de sistemas de alta e baixa pressão, com discussão sobre estruturas quentes e frias. | [Abrir no Colab](https://colab.research.google.com/github/RonaldRN/Monitorias_IAG-USP/blob/main/Meteorologia-Sinotica-I/Synoptic_charts_identification_High_Low_pressure_systems_GFS_analysis.ipynb) |
| **Análise isentrópica** | [`Isentropic_charts_GFS_analysis.ipynb`](Isentropic_charts_GFS_analysis.ipynb) | Cartas em superfícies isentrópicas para interpretar circulação, pressão e vorticidade potencial. | [Abrir no Colab](https://colab.research.google.com/github/RonaldRN/Monitorias_IAG-USP/blob/main/Meteorologia-Sinotica-I/Isentropic_charts_GFS_analysis.ipynb) |
| **Jatos polar e subtropical** | [`JET_POLAR_SUBTROPICAL.ipynb`](JET_POLAR_SUBTROPICAL.ipynb) | Identificação dos jatos de altos níveis e análise da estrutura espacial da circulação. | [Abrir no Colab](https://colab.research.google.com/github/RonaldRN/Monitorias_IAG-USP/blob/main/Meteorologia-Sinotica-I/JET_POLAR_SUBTROPICAL.ipynb) |
| **Jato de Baixos Níveis (SALLJ)** | [`IDENTIFICATION_SALLJ.ipynb`](IDENTIFICATION_SALLJ.ipynb) | Identificação e estudo do Jato de Baixos Níveis da América do Sul. | [Abrir no Colab](https://colab.research.google.com/github/RonaldRN/Monitorias_IAG-USP/blob/main/Meteorologia-Sinotica-I/IDENTIFICATION_SALLJ.ipynb) |
| **ZCIT: GOES-19 e GFS** | [`ZCIT_GOES19_GFS.ipynb`](ZCIT_GOES19_GFS.ipynb) | Investigação da Zona de Convergência Intertropical pela combinação de imagens de satélite e campos atmosféricos. | [Abrir no Colab](https://colab.research.google.com/github/RonaldRN/Monitorias_IAG-USP/blob/main/Meteorologia-Sinotica-I/ZCIT_GOES19_GFS.ipynb) |

### Arquivos auxiliares

| Arquivo | Finalidade |
|:--|:--|
| [`utilities_new_version.py`](utilities_new_version.py) | Rotinas auxiliares, incluindo funções para paletas de cores, acesso a dados e processamento de informações geoespaciais. Disponibilize o módulo no ambiente Python quando solicitado pelos notebooks. |
| [`IR4AVHRR6.cpt`](IR4AVHRR6.cpt) | Paleta CPT para representação gráfica de campos meteorológicos. |
| [`SVGAWVX_TEMP.cpt`](SVGAWVX_TEMP.cpt) | Paleta CPT para visualizações de temperatura. |

## 🎯 Principais temas de aprendizagem

### 🌡️ 1. Observações de superfície: estações automáticas do INMET

O notebook [`Download_INMET_AWS_data.ipynb`](Download_INMET_AWS_data.ipynb) é dedicado à obtenção e exploração de dados de **estações meteorológicas automáticas do Instituto Nacional de Meteorologia (INMET)**. Essas observações permitem associar a evolução temporal de variáveis de superfície à passagem ou à atuação de sistemas sinóticos.

Ao utilizar o material, recomenda-se verificar a identificação e localização da estação, o intervalo temporal, as variáveis disponíveis, as unidades, a referência de horário (UTC ou hora local) e eventuais valores ausentes. O procedimento de obtenção de dados pode depender da disponibilidade e das regras de serviços externos do INMET; consulte o código para verificar seus parâmetros específicos.

### 🗺️ 2. Cartas sinóticas com GFS e ERA5

Os notebooks de cartas sinóticas permitem representar campos meteorológicos em diferentes níveis e relacionar seus padrões espaciais aos sistemas atmosféricos. Estão disponíveis um [notebook principal do GFS](Synoptic_charts_GFS_analysis.ipynb), materiais [Parte I](Synoptic_charts_GFS_analysis_Part-I.ipynb) e [Parte II](Synoptic_charts_GFS_analysis_Part-II.ipynb), além de um [notebook com ERA5](Synoptic_chart_Reanalysis_ERA5.ipynb).

O [exercício de identificação de altas e baixas pressões](Synoptic_charts_identification_High_Low_pressure_systems_GFS_analysis.ipynb) complementa essa abordagem, permitindo discutir estruturas atmosféricas quentes e frias. Ao interpretar os campos, considere as diferenças entre **análises de modelos numéricos**, **previsões** e **reanálises**.

### 💨 3. Jatos atmosféricos

O notebook [`JET_POLAR_SUBTROPICAL.ipynb`](JET_POLAR_SUBTROPICAL.ipynb) aborda os **jatos polar e subtropical**, com foco em posição, intensidade e estrutura da circulação em altos níveis. O notebook [`IDENTIFICATION_SALLJ.ipynb`](IDENTIFICATION_SALLJ.ipynb) apresenta atividades relacionadas à identificação do **Jato de Baixos Níveis da América do Sul** (*South American Low-Level Jet*, SALLJ), importante para o estudo da circulação e do transporte de umidade em baixos níveis.

### 🌀 4. Análise isentrópica

O notebook [`Isentropic_charts_GFS_analysis.ipynb`](Isentropic_charts_GFS_analysis.ipynb) trabalha com cartas em superfícies de temperatura potencial constante. A abordagem ajuda a examinar o escoamento tridimensional e interpretar campos de vento, pressão e vorticidade potencial em situações sinóticas.

### 🛰️ 5. Zona de Convergência Intertropical

O notebook [`ZCIT_GOES19_GFS.ipynb`](ZCIT_GOES19_GFS.ipynb) integra observações de nebulosidade do satélite **GOES-19** e campos do **GFS** para analisar a Zona de Convergência Intertropical (ZCIT), relacionando padrões observados e circulação atmosférica.

## ▶️ Execução no Google Colab

O [Google Colab](https://colab.research.google.com/) permite executar os notebooks diretamente no navegador:

1. Na tabela acima, clique em **Abrir no Colab** ao lado do notebook desejado.
2. Examine as células iniciais e configure datas, regiões, caminhos e fontes de dados quando necessário.
3. Execute as células na sequência indicada, observando as instruções de instalação de bibliotecas.
4. Caso o notebook utilize `utilities_new_version.py` ou paletas `.cpt`, certifique-se de que os arquivos estejam acessíveis na sessão.

Para obter uma cópia da pasta em uma sessão **nova** do Colab, execute:

```python
!git clone https://github.com/RonaldRN/Monitorias_IAG-USP.git
%cd /content/Monitorias_IAG-USP/Meteorologia-Sinotica-I
```

> As sessões do Colab são temporárias: arquivos e pacotes instalados podem precisar ser preparados novamente depois de uma reinicialização.

## 🐍 Execução local e dependências

Para trabalhar com **JupyterLab**, **Jupyter Notebook** ou **VS Code**, clone o repositório:

```bash
git clone https://github.com/RonaldRN/Monitorias_IAG-USP.git
cd Monitorias_IAG-USP/Meteorologia-Sinotica-I
jupyter lab
```

Caso o repositório já esteja clonado, utilize `git pull origin main` a partir da sua pasta principal para recuperar novas alterações (desde que não haja conflitos locais).

Os notebooks usam bibliotecas do ecossistema científico Python. Entre os pacotes encontrados ou mencionados nos materiais estão `numpy`, `xarray`, `matplotlib`, `cartopy`, `netCDF4`, `MetPy`, `requests`, `boto3`, `cfgrib`, `pygrib` e `GDAL`. **Nem todos são necessários em cada notebook.** Verifique as células de importação e instalação do exercício escolhido. Pacotes como `GDAL` e ferramentas para GRIB podem exigir configurações específicas do sistema operacional.

## 🌐 Fontes de dados e boas práticas

| Fonte | Tipo de informação | Aplicação |
|:--|:--|:--|
| [INMET](https://portal.inmet.gov.br/) | Observações meteorológicas de superfície | Séries de estações automáticas e análise temporal. |
| [NOAA / GFS](https://www.ncei.noaa.gov/products/weather-climate-models/global-forecast) | Modelo global, análises e previsões | Cartas sinóticas e diagnósticos da circulação atmosférica. |
| [Copernicus / ERA5](https://cds.climate.copernicus.eu/) | Reanálise atmosférica | Estudos de situações meteorológicas históricas. |
| [NOAA / GOES](https://www.goes-r.gov/) | Observações de satélite geoestacionário | Imagens de nebulosidade e análise de sistemas atmosféricos. |

Ao elaborar figuras e interpretar resultados, registre **fonte, data, horário, nível de pressão, domínio geográfico, resolução e unidades**. Diferencie observações, análises, previsões e reanálises. Analise também a qualidade e a cobertura dos dados; a produção da figura é apenas uma etapa do diagnóstico meteorológico.

**Sugestão de roteiro de estudo:** comece pelas observações do INMET; passe às cartas do GFS e ERA5; examine estruturas de alta e baixa pressão; e avance para jatos, análise isentrópica e sensoriamento remoto. Os exercícios também podem ser usados de forma independente.

## 👨‍💻 Monitor PAE e contato

**Ronald Guiuseppi Ramírez Nina**  
Doutorando em Ciências Atmosféricas — IAG-USP  
Monitor/Estagiário PAE — Meteorologia Sinótica I

- **E-mail institucional:** [ronald.ramirez.nina@usp.br](mailto:ronald.ramirez.nina@usp.br)
- **E-mail alternativo:** [ronald.ramirez.nina@alumni.usp.br](mailto:ronald.ramirez.nina@alumni.usp.br)
- **GitHub:** [@RonaldRN](https://github.com/RonaldRN)

Em caso de dúvidas sobre a execução dos notebooks, o uso das bases de dados ou a interpretação meteorológica dos resultados, entre em contato.

---

**Material de apoio didático — Meteorologia Sinótica I | IAG-USP.**
