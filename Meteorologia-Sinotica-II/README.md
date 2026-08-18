# 🌎 Meteorologia Sinótica II — IAG/USP

Este diretório reúne **materiais computacionais de apoio à disciplina Meteorologia Sinótica II (ACA0523)** do Instituto de Astronomia, Geofísica e Ciências Atmosféricas da Universidade de São Paulo (IAG-USP).

Os códigos foram disponibilizados como material complementar às atividades da disciplina e do estágio do **Programa de Aperfeiçoamento de Ensino (PAE)**. O objetivo é auxiliar os estudantes na visualização e interpretação de diferentes sistemas e campos meteorológicos utilizados em análise sinótica.

> **Observação:** este repositório constitui material de apoio e não substitui as aulas, notas de aula ou demais materiais oficiais da disciplina.

---

## 👨‍💻 Monitor PAE

**Ronald Guiuseppi Ramírez Nina**
Doutorando em Ciências Atmosféricas — IAG/USP
Monitor/Estagiário PAE — Meteorologia Sinótica II

📧 **E-mail:** [ronald.ramirez.nina@alumni.usp.br](mailto:ronald.ramirez.nina@alumni.usp.br)
🐙 **GitHub:** [@RonaldRN](https://github.com/RonaldRN)

Em caso de dúvidas relacionadas aos códigos, execução dos notebooks ou interpretação dos produtos gerados, entrem em contato.

---

# 📂 Conteúdo deste diretório

Atualmente, a pasta `Meteorologia-Sinotica-II` contém os seguintes códigos:

| Arquivo                                | Descrição                                                                                                                                                                                                                                                         |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `JET_POLAR_SUBTROPICAL.ipynb`          | Elaboração de cartas sinóticas e análises destinadas à identificação do **Jato Subtropical (JST)** e do **Jato Polar (JP)**. Utiliza dados meteorológicos, incluindo campos do modelo **GFS**, e permite explorar a estrutura horizontal e vertical da atmosfera. |
| `Synoptic_chart_Reanalysis_ERA5.ipynb` | Construção de **cartas sinóticas utilizando dados da reanálise ERA5**, permitindo visualizar e combinar diferentes campos atmosféricos para a análise de sistemas meteorológicos.                                                                                 |
| `Synoptic_charts_GFS_analysis.ipynb`   | Construção de **cartas sinóticas a partir de dados de análise do modelo Global Forecast System (GFS)**, possibilitando a visualização de diferentes variáveis e níveis atmosféricos.                                                                              |
| `ZCIT_GOES19_GFS.ipynb`                | Análise da **Zona de Convergência Intertropical (ZCIT)** combinando imagens do satélite **GOES-19** com campos meteorológicos provenientes do **GFS**.                                                                                                            |
| `utilities_new_version.py`             | Conjunto de **funções auxiliares** utilizadas pelos notebooks, incluindo rotinas relacionadas ao download e processamento de dados de satélite GOES-19, transformações de coordenadas e reprojeção de dados.                                                      |

Os notebooks são arquivos no formato **Jupyter Notebook (`.ipynb`)**, nos quais texto explicativo, código Python e figuras podem ser executados de maneira interativa. Os códigos foram criados com o objetivo de ser executados na plataforma de Google-Colab. Porém, podem ser utilizados no computador pessoal do usuário.

---

# 📥 Como baixar o repositório

Existem duas formas principais de obter os códigos.

## Opção 1 — Clonar o repositório com Git

Esta é a opção recomendada para quem possui o **Git instalado**.

Abra um terminal e escolha a pasta na qual deseja salvar os materiais. Em seguida, execute:

```bash
git clone https://github.com/RonaldRN/Monitorias_IAG-USP.git
```

Após o download, entre no repositório:

```bash
cd Monitorias_IAG-USP
```

e depois na pasta de Meteorologia Sinótica II:

```bash
cd Meteorologia-Sinotica-II
```

A estrutura será semelhante a:

```text
Monitorias_IAG-USP/
│
└── Meteorologia-Sinotica-II/
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

1. Acesse a página principal do repositório `Monitorias_IAG-USP`;
2. Clique no botão verde **Code**;
3. Selecione **Download ZIP**;
4. Extraia o arquivo `.zip` em uma pasta de sua preferência;
5. Entre na pasta:

```text
Monitorias_IAG-USP/Meteorologia-Sinotica-II/
```

Os notebooks estarão disponíveis nesse diretório.

---

# 🔄 Como atualizar o repositório

Se o repositório foi clonado utilizando Git, não é necessário baixá-lo novamente quando novos códigos forem adicionados.

Entre na pasta:

```bash
cd Monitorias_IAG-USP
```

e execute:

```bash
git pull origin main
```

O Git irá baixar as atualizações mais recentes disponibilizadas no repositório.

---

# ▶️ Como executar os notebooks

Os arquivos `.ipynb` podem ser executados utilizando, por exemplo:

* **Google Colab**
* **Jupyter Notebook**
* **JupyterLab**
* **Visual Studio Code**, com a extensão Jupyter

Para usuários iniciantes, o **Google Colab** pode ser uma opção conveniente, pois permite executar notebooks diretamente no navegador.

Para execução local com Jupyter, entre na pasta:

```bash
cd Monitorias_IAG-USP/Meteorologia-Sinotica-II
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

Entre as bibliotecas utilizadas ao longo dos códigos estão:

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

Alguns notebooks também realizam o **download de dados meteorológicos diretamente de fontes externas**, portanto é necessária conexão com a internet durante determinadas etapas da execução.

---

# 🛰️ Dados meteorológicos

Dependendo do notebook, são utilizados diferentes conjuntos de dados, incluindo:

* **GFS — Global Forecast System**
* **ERA5 — ECMWF Reanalysis v5**
* **GOES-19 — Geostationary Operational Environmental Satellite**

Esses dados permitem analisar diferentes componentes da circulação atmosférica e identificar sistemas meteorológicos relevantes para Meteorologia Sinótica.

---

# 🎯 Objetivo do material

Mais do que simplesmente gerar figuras, a proposta dos notebooks é ajudar os estudantes a relacionar os conceitos discutidos em sala de aula com **dados atmosféricos reais**.

Recomenda-se observar não apenas o resultado final de cada código, mas também:

* quais variáveis meteorológicas estão sendo utilizadas;
* em quais níveis atmosféricos elas são analisadas;
* como os campos são combinados em uma carta sinótica;
* quais estruturas atmosféricas podem ser identificadas;
* e qual é a interpretação física dos padrões observados.

Os códigos podem ser modificados para explorar **outras datas, regiões, níveis atmosféricos e situações sinóticas**.

---

## 📚 IAG-USP — Ciências Atmosféricas

Material de apoio desenvolvido no contexto das atividades de **Meteorologia Sinótica II — IAG/USP**.

**Monitor PAE:** Ronald Guiuseppi Ramírez Nina
**Contato:** 
* [ronald.ramirez.nina@usp.br](mailto:ronald.ramirez.nina@usp.br)
* [ronald.ramirez.nina@alumni.usp.br](mailto:ronald.ramirez.nina@alumni.usp.br)
* [ronald.ramirez.nina@gmail.com](mailto:ronald.ramirez.nina@gmail.com)

