# 🌎 Meteorologia Sinótica I — IAG/USP

Este diretório reúne **materiais computacionais de apoio à disciplina Meteorologia Sinótica I (ACA0522)** do Instituto de Astronomia, Geofísica e Ciências Atmosféricas da Universidade de São Paulo (IAG-USP).

Os códigos são disponibilizados como material complementar às atividades da disciplina e das monitorias do **Programa de Aperfeiçoamento de Ensino (PAE)**. O objetivo é auxiliar os estudantes na visualização, análise e interpretação de diferentes campos e sistemas meteorológicos utilizados em Meteorologia Sinótica.

> ## 🚧 Em processo de atualização
>
> **Este diretório está em processo de atualização.**
>
> Novos notebooks, códigos e materiais de apoio serão adicionados ao longo da disciplina. A descrição apresentada neste README corresponde aos arquivos atualmente disponíveis no repositório.
>
> Recomenda-se consultar periodicamente esta pasta ou atualizar o repositório para ter acesso às versões e materiais mais recentes.

> **Observação:** este repositório constitui material de apoio e não substitui as aulas, notas de aula ou demais materiais oficiais da disciplina.

---

## 👨‍💻 Monitor PAE

**Ronald Guiuseppi Ramírez Nina**
Doutorando em Ciências Atmosféricas — IAG/USP
Monitor/Estagiário PAE — Meteorologia Sinótica I

📧 **E-mail:** [ronald.ramirez.nina@usp.br](mailto:ronald.ramirez.nina@usp.br)
📧 **E-mail:** [ronald.ramirez.nina@alumni.usp.br](mailto:ronald.ramirez.nina@alumni.usp.br)
🐙 **GitHub:** [@RonaldRN](https://github.com/RonaldRN)

Em caso de dúvidas relacionadas aos códigos, execução dos notebooks ou interpretação dos produtos gerados, entrem em contato.

---

# 📂 Conteúdo deste diretório

Atualmente, a pasta `Meteorologia-Sinotica-I` contém os seguintes materiais:

```text
Meteorologia-Sinotica-I/
│
├── JET_POLAR_SUBTROPICAL.ipynb
├── Synoptic_chart_Reanalysis_ERA5.ipynb
├── Synoptic_charts_GFS_analysis.ipynb
├── ZCIT_GOES19_GFS.ipynb
├── utilities_new_version.py
└── README.md
```

Os notebooks são arquivos no formato **Jupyter Notebook (`.ipynb`)**, nos quais textos explicativos, códigos Python e figuras podem ser executados de maneira interativa.

---

# 📚 Descrição dos códigos

| Arquivo                                | Descrição                                                                                                                                                                                                                                                                                                              |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `JET_POLAR_SUBTROPICAL.ipynb`          | Elaboração de cartas sinóticas e análises destinadas à identificação do **Jato Subtropical (JST)** e do **Jato Polar (JP)**. O notebook trabalha com campos meteorológicos do **GFS** e dados do **GOES-19**, além de permitir a análise da estrutura horizontal e vertical da atmosfera por meio de cortes verticais. |
| `Synoptic_chart_Reanalysis_ERA5.ipynb` | Construção de **cartas sinóticas utilizando dados da reanálise ERA5**, permitindo visualizar e combinar diferentes campos atmosféricos para identificação e interpretação de sistemas meteorológicos.                                                                                                                  |
| `Synoptic_charts_GFS_analysis.ipynb`   | Construção de **cartas sinóticas a partir de dados de análise do Global Forecast System (GFS)**, possibilitando a visualização de diferentes variáveis e níveis atmosféricos.                                                                                                                                          |
| `ZCIT_GOES19_GFS.ipynb`                | Análise da **Zona de Convergência Intertropical (ZCIT)** combinando imagens do satélite **GOES-19** com campos meteorológicos provenientes do **GFS**.                                                                                                                                                                 |
| `utilities_new_version.py`             | Conjunto de **funções auxiliares** utilizadas pelos notebooks, incluindo rotinas relacionadas ao download e processamento de dados do GOES-19, transformações de coordenadas, reprojeção de dados e outras operações necessárias para a geração dos produtos meteorológicos.                                           |

> 📌 **Importante:** novos códigos serão adicionados posteriormente. Portanto, esta lista será atualizada à medida que novos materiais forem disponibilizados.

---

# 💨 Jatos de altos níveis

O notebook:

```text
JET_POLAR_SUBTROPICAL.ipynb
```

foi desenvolvido para auxiliar na identificação e análise do:

* **Jato Subtropical (JST)**;
* **Jato Polar (JP)**;
* diferentes ramos do Jato Polar;
* estrutura horizontal dos campos de vento em altos níveis;
* estrutura vertical dos jatos.

O notebook inclui rotinas para obtenção e processamento de dados meteorológicos e permite construir **cortes verticais em latitude e longitude**, possibilitando analisar a posição e a estrutura vertical das correntes de jato.

---

# 🌦️ Cartas sinóticas

Os notebooks:

```text
Synoptic_chart_Reanalysis_ERA5.ipynb
Synoptic_charts_GFS_analysis.ipynb
```

permitem construir cartas sinóticas utilizando duas importantes fontes de dados atmosféricos:

### ERA5

A **ERA5** é uma reanálise atmosférica que permite analisar campos meteorológicos de períodos passados de forma espacial e temporalmente consistente.

### GFS

O **Global Forecast System (GFS)** é um modelo global de previsão numérica do tempo. Os notebooks permitem trabalhar com campos de análise e explorar diferentes variáveis e níveis atmosféricos.

Esses códigos podem ser utilizados para relacionar os conceitos discutidos em sala de aula com situações atmosféricas reais.

---

# 🛰️ GOES-19 e Zona de Convergência Intertropical

O notebook:

```text
ZCIT_GOES19_GFS.ipynb
```

combina informações provenientes de:

```text
GOES-19
   +
  GFS
```

para auxiliar na análise da **Zona de Convergência Intertropical (ZCIT)**.

A combinação de imagens de satélite com campos meteorológicos permite relacionar a distribuição de nebulosidade observada pelo satélite com a circulação atmosférica representada pelos dados do modelo.

---

# 🔧 Arquivo `utilities_new_version.py`

O arquivo:

```text
utilities_new_version.py
```

contém diversas funções auxiliares utilizadas pelos notebooks.

Entre elas estão rotinas associadas a:

* download de dados do **GOES-19**;
* acesso a produtos do **ABI**;
* acesso a dados do **GLM**;
* conversão entre sistemas de coordenadas;
* transformação das coordenadas da projeção do satélite;
* reprojeção de imagens para latitude e longitude;
* processamento de arquivos NetCDF;
* manipulação de dados utilizados na elaboração das figuras.

Por isso, quando um notebook utilizar este módulo, é importante manter o arquivo `utilities_new_version.py` disponível no mesmo ambiente de trabalho ou no caminho especificado pelo código.

---

# 📥 Como baixar o repositório

Existem duas formas principais de obter os códigos.

## Opção 1 — Clonar o repositório com Git

Esta é a opção recomendada para quem já possui o **Git instalado**.

Abra um terminal e execute:

```bash
git clone https://github.com/RonaldRN/Monitorias_IAG-USP.git
```

Depois entre no repositório:

```bash
cd Monitorias_IAG-USP
```

e acesse a pasta de Meteorologia Sinótica I:

```bash
cd Meteorologia-Sinotica-I
```

A estrutura será semelhante a:

```text
Monitorias_IAG-USP/
│
└── Meteorologia-Sinotica-I/
    │
    ├── JET_POLAR_SUBTROPICAL.ipynb
    ├── Synoptic_chart_Reanalysis_ERA5.ipynb
    ├── Synoptic_charts_GFS_analysis.ipynb
    ├── ZCIT_GOES19_GFS.ipynb
    ├── utilities_new_version.py
    └── README.md
```

---

## Opção 2 — Baixar como arquivo ZIP

Caso você não utilize Git:

1. Acesse o repositório:

   `https://github.com/RonaldRN/Monitorias_IAG-USP`

2. Clique no botão verde **Code**;

3. Selecione **Download ZIP**;

4. Extraia o arquivo `.zip` em uma pasta de sua preferência;

5. Entre na pasta:

```text
Monitorias_IAG-USP/Meteorologia-Sinotica-I/
```

Os notebooks e arquivos auxiliares estarão disponíveis nesse diretório.

---

# 🔄 Como atualizar o repositório

Como novos materiais serão adicionados ao longo da disciplina, os estudantes que utilizaram `git clone` podem atualizar sua cópia local sem precisar baixar novamente todo o repositório.

Entre na pasta:

```bash
cd Monitorias_IAG-USP
```

e execute:

```bash
git pull origin main
```

O Git irá baixar as atualizações e os novos arquivos disponibilizados no repositório.

> 💡 **Recomendação:** como a pasta de Meteorologia Sinótica I está em processo de atualização, execute periodicamente `git pull origin main` quando for informado que novos materiais foram adicionados.

---

# ☁️ Utilização no Google Drive e Google Colab

Para facilitar a execução dos códigos, os notebooks podem ser utilizados no **Google Colab**.

Depois de clonar ou baixar o repositório, recomenda-se fazer o upload da pasta ou dos arquivos necessários para o **Google Drive**.

Uma possível organização é:

```text
Meu Drive/
│
└── Meteorologia_Sinotica_I/
    │
    ├── JET_POLAR_SUBTROPICAL.ipynb
    ├── Synoptic_chart_Reanalysis_ERA5.ipynb
    ├── Synoptic_charts_GFS_analysis.ipynb
    ├── ZCIT_GOES19_GFS.ipynb
    └── utilities_new_version.py
```

Para abrir um notebook:

1. Acesse o **Google Drive**;
2. Localize o arquivo `.ipynb`;
3. Clique com o botão direito sobre o arquivo;
4. Selecione **Abrir com → Google Colaboratory**;
5. Execute as células seguindo a ordem indicada no notebook.

---

# ▶️ Como executar os notebooks

Os arquivos `.ipynb` também podem ser executados utilizando:

* **Google Colab**
* **Jupyter Notebook**
* **JupyterLab**
* **Visual Studio Code**, com a extensão Jupyter

Para usuários iniciantes, o **Google Colab** é uma opção conveniente, pois permite executar os notebooks diretamente no navegador.

Para execução local com Jupyter, entre na pasta:

```bash
cd Monitorias_IAG-USP/Meteorologia-Sinotica-I
```

e execute:

```bash
jupyter notebook
```

ou:

```bash
jupyter lab
```

Em seguida, selecione o notebook desejado.

---

# 🐍 Bibliotecas Python

Os notebooks utilizam diferentes bibliotecas do ecossistema científico Python para leitura, processamento, análise e visualização de dados meteorológicos.

Entre as bibliotecas utilizadas nos códigos estão:

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

As dependências podem variar de acordo com o notebook utilizado.

Alguns notebooks instalam automaticamente parte dessas bibliotecas quando executados no **Google Colab**.

---

# 🌐 Conexão com a internet

Alguns códigos realizam o **download de dados meteorológicos diretamente de fontes externas**.

Portanto, durante determinadas etapas da execução, é necessária uma conexão com a internet.

Também é importante verificar a data utilizada no notebook, pois a disponibilidade dos dados pode depender da fonte meteorológica utilizada.

---

# 🛰️ Dados meteorológicos

Dependendo do notebook, são utilizados diferentes conjuntos de dados, incluindo:

* **GFS — Global Forecast System**
* **ERA5 — ECMWF Reanalysis v5**
* **GOES-19 — Geostationary Operational Environmental Satellite**

A combinação desses dados permite analisar diferentes componentes da circulação atmosférica e relacionar observações de satélite com campos atmosféricos derivados de modelos e reanálises.

---

# 🎯 Objetivo do material

Mais do que simplesmente executar códigos e gerar figuras, a proposta dos notebooks é ajudar os estudantes a desenvolver uma **interpretação meteorológica dos campos atmosféricos**.

Ao utilizar os códigos, recomenda-se observar:

* qual variável meteorológica está sendo representada;
* qual é sua unidade;
* em qual nível atmosférico ela está sendo analisada;
* como os diferentes campos se relacionam;
* quais padrões de circulação podem ser identificados;
* como reconhecer estruturas atmosféricas em cartas sinóticas;
* como relacionar imagens de satélite com os campos meteorológicos;
* e qual é a interpretação física dos padrões observados.

Os códigos podem ser modificados para explorar **outras datas, regiões, níveis atmosféricos e situações sinóticas**.

---

# 🚧 Próximas atualizações

Esta pasta continuará recebendo novos materiais ao longo da disciplina.

Entre as atualizações poderão ser adicionados:

* novos notebooks;
* novos exemplos de situações sinóticas;
* códigos auxiliares;
* exercícios;
* materiais de apoio;
* e atualizações das rotinas já disponíveis.

Portanto, consulte periodicamente:

```text
Meteorologia-Sinotica-I/
```

para verificar os materiais mais recentes.

---

## 📚 IAG-USP — Ciências Atmosféricas

Material de apoio desenvolvido no contexto das atividades de **Meteorologia Sinótica I (ACA0522) — IAG/USP**.

**Monitor PAE:** Ronald Guiuseppi Ramírez Nina

**Contato:**

* [ronald.ramirez.nina@usp.br](mailto:ronald.ramirez.nina@usp.br)
* [ronald.ramirez.nina@alumni.usp.br](mailto:ronald.ramirez.nina@alumni.usp.br)
* [GitHub — @RonaldRN](https://github.com/RonaldRN)

> 🚧 **Material em processo de atualização — novos códigos e conteúdos serão adicionados ao repositório.**

