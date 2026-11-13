# 🌎 Meteorologia Sinótica I — IAG/USP

**Disciplina:** Meteorologia Sinótica I (ACA0522)  
**Instituição:** Instituto de Astronomia, Geofísica e Ciências Atmosféricas da Universidade de São Paulo (IAG-USP)  
**Material:** notebooks Jupyter e códigos Python de apoio didático

Este diretório reúne materiais computacionais desenvolvidos e organizados no contexto das atividades de **monitoria e do Programa de Aperfeiçoamento de Ensino (PAE)** da disciplina **Meteorologia Sinótica I**. O objetivo é auxiliar os estudantes na elaboração de cartas sinóticas e na **visualização, identificação e interpretação de sistemas e processos atmosféricos** utilizando dados meteorológicos reais.

Os materiais abordam aplicações com o **Global Forecast System (GFS)**, a **reanálise ERA5** e imagens do satélite **GOES-19**, integrando conceitos apresentados em aula e ferramentas de análise científica em Python.

> **Nota didática:** este repositório oferece material complementar e **não substitui** as aulas, notas de aula ou demais materiais oficiais da disciplina. O conteúdo pode ser ampliado e atualizado ao longo das atividades de monitoria.

## 📑 Navegação

- [Materiais disponíveis](#-materiais-disponíveis)
- [Temas e objetivos de aprendizagem](#-temas-e-objetivos-de-aprendizagem)
- [Como executar os notebooks](#-como-executar-os-notebooks)
- [Instalação e dependências](#-instalação-e-dependências)
- [Dados meteorológicos](#-dados-meteorológicos)
- [Orientações para utilização](#-orientações-para-utilização)
- [Monitor PAE e contato](#-monitor-pae-e-contato)

## 📂 Materiais disponíveis

| Arquivo | Conteúdo principal |
|:--|:--|
| [`JET_POLAR_SUBTROPICAL.ipynb`](JET_POLAR_SUBTROPICAL.ipynb) | Identificação e análise do **Jato Subtropical (JST)** e do **Jato Polar (JP)**. Combina campos do GFS e dados do GOES-19 e permite investigar a estrutura horizontal e vertical dos jatos por meio de seções verticais. |
| [`Synoptic_chart_Reanalysis_ERA5.ipynb`](Synoptic_chart_Reanalysis_ERA5.ipynb) | Elaboração de **cartas sinóticas com a reanálise ERA5** e combinação de campos atmosféricos para diagnóstico e interpretação de sistemas meteorológicos. |
| [`Synoptic_charts_GFS_analysis.ipynb`](Synoptic_charts_GFS_analysis.ipynb) | Construção de **cartas sinóticas com análises do GFS**, explorando diferentes variáveis e níveis atmosféricos. |
| [`ZCIT_GOES19_GFS.ipynb`](ZCIT_GOES19_GFS.ipynb) | Investigação da **Zona de Convergência Intertropical (ZCIT)** pela análise conjunta de imagens do GOES-19 e campos do GFS. |
| [`utilities_new_version.py`](utilities_new_version.py) | Funções auxiliares para acesso e processamento de dados de satélite, manipulação de arquivos e transformações ou reprojeções de coordenadas. |

Os arquivos `.ipynb` são *Jupyter Notebooks*: documentos interativos que combinam código Python, explicações e figuras. O arquivo `.py` contém funções auxiliares que podem ser importadas pelos notebooks.

### Organização da pasta

```text
Meteorologia-Sinotica-I/
├── JET_POLAR_SUBTROPICAL.ipynb
├── Synoptic_chart_Reanalysis_ERA5.ipynb
├── Synoptic_charts_GFS_analysis.ipynb
├── ZCIT_GOES19_GFS.ipynb
├── utilities_new_version.py
└── README.md
```

## 🎯 Temas e objetivos de aprendizagem

### 💨 Jatos de altos níveis

O notebook [`JET_POLAR_SUBTROPICAL.ipynb`](JET_POLAR_SUBTROPICAL.ipynb) permite explorar a posição e a estrutura dos jatos atmosféricos, com atenção especial ao **Jato Subtropical** e ao **Jato Polar**. As representações horizontais e as seções verticais auxiliam na investigação da intensidade dos ventos, da distribuição espacial dos máximos e da estrutura da circulação em altitude.

### 🌦️ Cartas sinóticas com GFS e ERA5

Os notebooks [`Synoptic_charts_GFS_analysis.ipynb`](Synoptic_charts_GFS_analysis.ipynb) e [`Synoptic_chart_Reanalysis_ERA5.ipynb`](Synoptic_chart_Reanalysis_ERA5.ipynb) permitem elaborar cartas meteorológicas e relacionar a distribuição de diferentes campos atmosféricos com a identificação de sistemas sinóticos.

**GFS** é um sistema global de previsão numérica do tempo, cujas análises representam o estado estimado da atmosfera em um determinado horário. **ERA5** é uma reanálise que combina observações e modelagem numérica para produzir um conjunto espacial e temporalmente consistente de campos atmosféricos históricos.

Ao interpretar as cartas, recomenda-se observar a relação entre as variáveis representadas, a altitude ou o nível de pressão, a posição geográfica dos sistemas e os mecanismos físicos associados.

### 🛰️ Zona de Convergência Intertropical (ZCIT)

O notebook [`ZCIT_GOES19_GFS.ipynb`](ZCIT_GOES19_GFS.ipynb) combina imagens do satélite GOES-19 e informações do GFS. Essa abordagem permite comparar os padrões de nebulosidade observados por sensoriamento remoto com os campos de circulação atmosférica utilizados no diagnóstico da **ZCIT**.

### 🔧 Funções auxiliares

O módulo [`utilities_new_version.py`](utilities_new_version.py) reúne rotinas de suporte, incluindo operações relacionadas aos produtos dos sensores **ABI** e **GLM** do GOES-19, ao processamento de arquivos NetCDF e à transformação ou reprojeção de coordenadas.

> **Atenção:** quando um notebook importar `utilities_new_version.py`, o arquivo precisa estar acessível ao ambiente Python — por exemplo, no mesmo diretório de execução ou em um caminho incluído no `sys.path`.

## ▶️ Como executar os notebooks

### Opção 1 — Google Colab

O [Google Colab](https://colab.research.google.com/) permite executar notebooks em um ambiente Python acessado pelo navegador.

1. Abra a pasta [`Meteorologia-Sinotica-I`](https://github.com/RonaldRN/Monitorias_IAG-USP/tree/main/Meteorologia-Sinotica-I) no GitHub.
2. Selecione o notebook desejado ou abra o Colab e escolha a opção de importar um notebook do GitHub.
3. Selecione o ambiente de execução e execute as células **na ordem apresentada**.
4. Caso o notebook utilize o arquivo `utilities_new_version.py`, disponibilize esse módulo no ambiente de execução antes de importá-lo.

Para disponibilizar os arquivos do repositório em uma sessão do Colab, uma alternativa é executar em uma célula:

```python
!git clone https://github.com/RonaldRN/Monitorias_IAG-USP.git
%cd /content/Monitorias_IAG-USP/Meteorologia-Sinotica-I
```

> A sessão do Colab é temporária: arquivos baixados e instalados no ambiente podem precisar ser preparados novamente após a reinicialização. Os comandos acima destinam-se a uma sessão em que o repositório ainda não tenha sido clonado.

### Opção 2 — Execução local (Jupyter ou VS Code)

Com **Git** e um ambiente Python/Jupyter instalados, clone o repositório:

```bash
git clone https://github.com/RonaldRN/Monitorias_IAG-USP.git
cd Monitorias_IAG-USP/Meteorologia-Sinotica-I
```

Para abrir os notebooks com Jupyter, execute:

```bash
jupyter lab
```

Também é possível utilizar `jupyter notebook` ou abrir os arquivos `.ipynb` no **Visual Studio Code**, com a extensão Jupyter.

### Opção 3 — Download em ZIP

Na [página principal do repositório](https://github.com/RonaldRN/Monitorias_IAG-USP), selecione **Code → Download ZIP**, extraia os arquivos e abra a pasta `Meteorologia-Sinotica-I` no programa de sua preferência.

### Atualização da cópia local

Se o repositório foi clonado com Git, acesse sua pasta principal e execute:

```bash
git pull origin main
```

Esse comando recupera as atualizações disponíveis na branch `main`, desde que alterações locais não impeçam a integração.

## 🐍 Instalação e dependências

Os notebooks utilizam bibliotecas do ecossistema científico Python, conforme a atividade. Entre as dependências mencionadas nos materiais estão:

```text
numpy
xarray
matplotlib
cartopy
netCDF4
MetPy
requests
boto3
pygrib
cfgrib
GDAL
```

**Não é necessário instalar todas as bibliotecas para executar um único notebook.** Consulte as primeiras células do arquivo escolhido para verificar quais pacotes e recursos são utilizados. Em algumas situações, dependências como `pygrib`, `cfgrib` e `GDAL` exigem configuração adicional, sobretudo em ambientes locais.

Algumas atividades requerem conexão com a internet para obter os dados, e o sucesso do download depende da disponibilidade do serviço externo, do período selecionado e do formato do produto meteorológico.

## 🌐 Dados meteorológicos

| Fonte | Tipo de dados | Aplicação didática |
|:--|:--|:--|
| **GFS** (*Global Forecast System*) | Análises e campos produzidos por modelo numérico global | Elaboração de cartas sinóticas e análise da circulação atmosférica. |
| **ERA5** | Reanálise atmosférica | Investigação de situações meteorológicas históricas. |
| **GOES-19** | Observações de satélite geoestacionário | Análise de nebulosidade e integração com informações dinâmicas da atmosfera. |

Os produtos do GOES-19 utilizados nos códigos podem envolver dados dos sensores **ABI** (*Advanced Baseline Imager*) e **GLM** (*Geostationary Lightning Mapper*), conforme a aplicação. A disponibilidade dos arquivos pode variar com a data e a fonte de acesso.

## 🧭 Orientações para utilização

O propósito das atividades é **interpretar os resultados meteorologicamente**, e não apenas produzir figuras. Ao utilizar os notebooks, procure:

1. Identificar a **fonte de dados**, o horário analisado e a região geográfica.
2. Verificar as **unidades**, os níveis de pressão e o significado físico de cada variável.
3. Examinar a combinação dos campos para reconhecer padrões de circulação e sistemas meteorológicos.
4. Comparar as informações dos diferentes níveis atmosféricos e, quando aplicável, as observações por satélite.
5. Registrar as hipóteses e as limitações da análise, distinguindo observações, análises de modelos e reanálises.

Os notebooks podem servir como ponto de partida para explorar outras datas, domínios geográficos e configurações de visualização, respeitando a disponibilidade dos dados e as limitações do código.

## 👨‍💻 Monitor PAE e contato

**Ronald Guiuseppi Ramírez Nina**  
Doutorando em Ciências Atmosféricas — IAG-USP  
Monitor/Estagiário PAE — Meteorologia Sinótica I

- **E-mail institucional:** [ronald.ramirez.nina@usp.br](mailto:ronald.ramirez.nina@usp.br)
- **E-mail alternativo:** [ronald.ramirez.nina@alumni.usp.br](mailto:ronald.ramirez.nina@alumni.usp.br)
- **GitHub:** [@RonaldRN](https://github.com/RonaldRN)

Em caso de dúvidas relacionadas à execução dos códigos ou à interpretação dos produtos, entre em contato.

---

**Material de apoio didático — Meteorologia Sinótica I | IAG-USP.**
