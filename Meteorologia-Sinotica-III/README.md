# 🌎 Meteorologia Sinótica III — IAG/USP

Este diretório reúne **materiais computacionais de apoio à disciplina Meteorologia Sinótica III (ACA0524)** do Instituto de Astronomia, Geofísica e Ciências Atmosféricas da Universidade de São Paulo (IAG-USP).

Os códigos foram disponibilizados como material complementar às atividades da disciplina e do estágio do **Programa de Aperfeiçoamento de Ensino (PAE)**. O objetivo é auxiliar os estudantes na análise e interpretação de sistemas meteorológicos, utilizando dados atmosféricos reais, ferramentas computacionais e diferentes metodologias aplicadas à Meteorologia Sinótica.

Entre os temas abordados nos códigos estão a análise e o rastreamento de ciclones, a construção de diagramas de Hovmöller e perfis verticais, o cálculo de balanços atmosféricos com o **ATMOS-BUD**, a utilização da reanálise **ERA5** e a análise de precipitação com o produto **IMERG**.

> **Observação:** este repositório constitui material de apoio e não substitui as aulas, notas de aula ou demais materiais oficiais da disciplina. Grande parte dos notebooks foi preparada para execução na plataforma **Google Colab**, embora alguns códigos também possam ser executados localmente. Os scripts em GrADS (`.gs`) requerem uma instalação do **GrADS** para sua execução.

---

## 👨‍💻 Monitor PAE

**Ronald Guiuseppi Ramírez Nina**
Doutorando em Ciências Atmosféricas — IAG/USP
Monitor/Estagiário PAE — Meteorologia Sinótica III

* 📧 **E-mail:** [ronald.ramirez.nina@usp.br](mailto:ronald.ramirez.nina@usp.br)
* 📧 **E-mail:** [ronald.ramirez.nina@alumni.usp.br](mailto:ronald.ramirez.nina@alumni.usp.br)
* 📧 **E-mail:** [ronald.ramirez.nina@gmail.com](mailto:ronald.ramirez.nina@gmail.com)
* 🐙 **GitHub:** [@RonaldRN](https://github.com/RonaldRN)

Em caso de dúvidas relacionadas aos códigos, execução dos notebooks ou interpretação dos produtos gerados, entrem em contato.

---

# 📂 Conteúdo deste diretório

A pasta `Meteorologia-Sinotica-III` está organizada em quatro conjuntos principais de materiais:

```text
Meteorologia-Sinotica-III/
│
├── Google-Colab_ATMOSBUD/
│
├── Hovmoller_Vertical-profiles/
│
├── climatology_index-ZCAS-LISAM/
│
└── track_cyclones/
```

Cada diretório corresponde a uma atividade ou conjunto de análises desenvolvido no contexto da disciplina.

---

# 🌪️ 1. `Google-Colab_ATMOSBUD`

Este diretório contém notebooks destinados à execução e utilização do **ATMOS-BUD** no Google Colab.

O ATMOS-BUD é utilizado para realizar análises de balanços atmosféricos acompanhando a evolução de sistemas meteorológicos, como ciclones, por meio de um domínio móvel definido a partir da trajetória do sistema.

O fluxo geral utilizado nos notebooks é:

```text
ERA5
  │
  ▼
Download dos campos meteorológicos
  │
  ▼
Construção da trajetória do ciclone
  │
  ▼
track_<cyclone_name>.txt
  │
  ▼
ATMOS-BUD
  │
  ▼
Balanços atmosféricos
```

### Arquivos principais

| Arquivo                                | Descrição                                                                                                                                                                                                                           |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Access_to_Reanalysis_ERA5.ipynb`      | Realiza o acesso e download dos campos meteorológicos da **reanálise ERA5** necessários para as análises. Os dados são armazenados em arquivos NetCDF que posteriormente podem ser utilizados pelo ATMOS-BUD.                       |
| `track_file.ipynb`                     | Auxilia na construção do arquivo de trajetória do ciclone, contendo informações como tempo, latitude, longitude e dimensões do domínio utilizado para acompanhar o sistema.                                                         |
| `ATMOSBUD_Google_Colab.ipynb`          | Configura e executa o **ATMOS-BUD diretamente no Google Colab**, incluindo clonagem do repositório, instalação de dependências, conexão ao Google Drive, configuração dos arquivos de entrada e execução dos balanços atmosféricos. |
| `Synoptic_chart_Reanalysis_ERA5.ipynb` | Gera **cartas sinóticas utilizando a reanálise ERA5**, permitindo analisar o ambiente atmosférico de grande escala associado ao ciclone antes, durante e depois de sua evolução.                                                    |
| `README.md`                            | Contém instruções específicas e detalhadas para a utilização do fluxo ATMOS-BUD no Google Colab.                                                                                                                                    |

Para aplicações com um domínio que acompanha o ciclone, o ATMOS-BUD utiliza um arquivo de trajetória com estrutura semelhante a:

```text
time;Lat;Lon;length;width
YYYY-MM-DD-HHMM;latitude;longitude;length;width
```

É importante que os tempos presentes no arquivo de trajetória correspondam aos tempos disponíveis no arquivo ERA5 utilizado como entrada.

---

# 📊 2. `Hovmoller_Vertical-profiles`

Este diretório contém notebooks destinados à análise da **estrutura temporal e vertical dos termos dos balanços atmosféricos associados à evolução de ciclones**.

Os códigos utilizam resultados previamente produzidos pelo ATMOS-BUD.

### Arquivos

| Arquivo                                  | Descrição                                                                                                                                                                                           |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Hovmoller-ciclones.ipynb`               | Produz diagramas do tipo **Hovmöller** para acompanhar a evolução temporal e vertical dos diferentes termos dos balanços atmosféricos durante o ciclo de vida de um ciclone.                        |
| `vertical_profile_phases_ciclones.ipynb` | Calcula e compara **perfis verticais dos termos dos balanços atmosféricos** em diferentes fases do ciclo de vida do ciclone, como fase incipiente, intensificação, fase madura e desintensificação. |

Entre os balanços analisados nos notebooks estão:

* **Balanço de calor**
* **Balanço de vorticidade**
* **Balanço de umidade**

Essa abordagem permite investigar não apenas a evolução horizontal do ciclone, mas também como diferentes processos físicos atuam ao longo da coluna atmosférica durante suas diferentes fases de desenvolvimento.

---

# 🌧️ 3. `climatology_index-ZCAS-LISAM`

Este diretório reúne notebooks relacionados à análise climatológica da precipitação e às atividades envolvendo a **Zona de Convergência do Atlântico Sul (ZCAS)** e o índice **LISAM**.

Os códigos utilizam dados do produto de precipitação por satélite **IMERG — Integrated Multi-satellitE Retrievals for GPM**.

### Arquivos

| Arquivo                             | Descrição                                                                                                                                                                                              |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Climatology_IMERG_Final_Run.ipynb` | Processa dados **IMERG Final Run**, realiza a acumulação diária da precipitação e constrói uma climatologia baseada em **pentadas**, permitindo analisar a distribuição climatológica da precipitação. |
| `IMERG_LATE.ipynb`                  | Notebook destinado ao processamento e utilização dos dados **IMERG Late Run** no contexto das atividades relacionadas à precipitação e à identificação/análise de episódios de ZCAS.                   |

No notebook de climatologia, os dados diários são organizados em períodos de cinco dias (**pentadas**), permitindo construir uma climatologia pentadal utilizada como referência para comparar episódios individuais de precipitação.

Esse tipo de análise ajuda a distinguir condições climatológicas de situações com precipitação anômala e persistente, importantes para o estudo de sistemas como a ZCAS.

---

# 🌀 4. `track_cyclones`

Este diretório contém ferramentas para **download de dados ERA5, visualização e rastreamento da trajetória de ciclones**.

São disponibilizadas rotinas em Python e GrADS, permitindo explorar diferentes metodologias de identificação e acompanhamento dos sistemas.

### Principais arquivos

| Arquivo                                             | Descrição                                                                                                                                                                                                                                        |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Extrair_coords_time-lat-lon-length-width.py`       | Ferramenta interativa em Python para rastrear um ciclone a partir de um arquivo NetCDF. Permite desenhar uma caixa ao redor do sistema e salvar, para cada tempo, o centro da caixa e suas dimensões (`time`, `Lat`, `Lon`, `length` e `width`). |
| `Extrair_coords_time-lat-lon.gs`                    | Script em **GrADS** utilizado para auxiliar na identificação e extração da posição do centro de um ciclone ao longo do tempo.                                                                                                                    |
| `Extrair_coords_time-lat-lon_ciclone-original.gs`   | Versão da rotina GrADS utilizada para rastreamento do centro do ciclone.                                                                                                                                                                         |
| `Extrair_coords_time-lat-lon_ciclone-automatico.gs` | Versão automatizada da rotina em GrADS para identificação e acompanhamento do centro do ciclone ao longo dos diferentes tempos da análise.                                                                                                       |
| `era5_sinotica3.py`                                 | Script utilizando a **CDS API** para baixar dados ERA5 em níveis de pressão, incluindo geopotencial, temperatura, umidade específica, componentes zonal e meridional do vento e velocidade vertical.                                             |
| `era5_sinotica3_mslp.py`                            | Script para download da **pressão ao nível médio do mar (MSLP)** da reanálise ERA5.                                                                                                                                                              |
| `track_ciclone_2025.txt`                            | Exemplo de arquivo contendo a trajetória de um ciclone.                                                                                                                                                                                          |
| `track_ciclone_2025_automatico.txt`                 | Exemplo de trajetória obtida com a rotina automática de rastreamento.                                                                                                                                                                            |

O diretório também contém arquivos auxiliares utilizados pelas rotinas de visualização, como:

```text
ne_110m_coastline/
brmap
cbarn.gs
```

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

e depois na pasta de Meteorologia Sinótica III:

```bash
cd Meteorologia-Sinotica-III
```

A estrutura será semelhante a:

```text
Monitorias_IAG-USP/
│
└── Meteorologia-Sinotica-III/
    │
    ├── Google-Colab_ATMOSBUD/
    │   ├── ATMOSBUD_Google_Colab.ipynb
    │   ├── Access_to_Reanalysis_ERA5.ipynb
    │   ├── Synoptic_chart_Reanalysis_ERA5.ipynb
    │   ├── track_file.ipynb
    │   └── README.md
    │
    ├── Hovmoller_Vertical-profiles/
    │   ├── Hovmoller-ciclones.ipynb
    │   └── vertical_profile_phases_ciclones.ipynb
    │
    ├── climatology_index-ZCAS-LISAM/
    │   ├── Climatology_IMERG_Final_Run.ipynb
    │   └── IMERG_LATE.ipynb
    │
    └── track_cyclones/
        ├── Extrair_coords_time-lat-lon-length-width.py
        ├── Extrair_coords_time-lat-lon.gs
        ├── Extrair_coords_time-lat-lon_ciclone-automatico.gs
        ├── Extrair_coords_time-lat-lon_ciclone_original.gs
        ├── era5_sinotica3.py
        ├── era5_sinotica3_mslp.py
        ├── track_ciclone_2025.txt
        └── track_ciclone_2025_automatico.txt
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
Monitorias_IAG-USP/Meteorologia-Sinotica-III/
```

Os notebooks e demais códigos estarão disponíveis dentro das respectivas subpastas.

---

# ☁️ Utilização com Google Drive e Google Colab

Para os notebooks preparados para execução no **Google Colab**, recomenda-se copiar os arquivos necessários para o Google Drive.

Uma possível organização é:

```text
Meu Drive/
│
└── Meteorologia_Sinotica_III/
    │
    ├── Google-Colab_ATMOSBUD/
    ├── Hovmoller_Vertical-profiles/
    ├── climatology_index-ZCAS-LISAM/
    └── dados/
```

Depois de fazer o upload dos notebooks:

1. Acesse o **Google Drive**;
2. Localize o arquivo `.ipynb`;
3. Clique com o botão direito sobre o notebook;
4. Selecione **Abrir com → Google Colaboratory**;
5. Execute as células seguindo a ordem apresentada no notebook.

Alguns notebooks conectam diretamente o Google Colab ao Google Drive. Portanto, verifique sempre os caminhos definidos no início do código e adapte-os à organização das pastas do seu próprio Drive.

Por exemplo:

```python
/content/drive/MyDrive/Meteorologia_Sinotica_III/
```

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

Para usuários iniciantes, o **Google Colab** é a opção recomendada para os notebooks deste diretório, pois permite executar os códigos diretamente no navegador e facilita a integração com o Google Drive.

Para execução local com Jupyter, entre na pasta:

```bash
cd Monitorias_IAG-USP/Meteorologia-Sinotica-III
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

# 🖥️ Scripts GrADS

Algumas rotinas de rastreamento de ciclones possuem extensão:

```text
.gs
```

Esses arquivos são scripts para o **GrADS — Grid Analysis and Display System** e não são executados diretamente no Google Colab da mesma forma que os notebooks Python.

Para utilizá-los é necessário possuir o GrADS instalado e executar, por exemplo:

```bash
grads -l
```

e, dentro do GrADS:

```text
run Extrair_coords_time-lat-lon.gs
```

Essas rotinas são disponibilizadas principalmente como apoio às atividades de rastreamento e análise de ciclones.

---

# 🐍 Bibliotecas Python

Os notebooks e scripts utilizam diferentes bibliotecas do ecossistema científico Python para leitura, processamento, análise e visualização de dados meteorológicos.

Entre as bibliotecas utilizadas estão:

```text
numpy
pandas
xarray
matplotlib
cartopy
netCDF4
cdsapi
```

Dependendo do notebook ou atividade, outras bibliotecas podem ser instaladas automaticamente durante a execução no Google Colab.

Alguns códigos também realizam **downloads de dados meteorológicos diretamente de fontes externas**, sendo necessária conexão com a internet.

---

# 🛰️ Dados e ferramentas meteorológicas

Os materiais deste diretório utilizam principalmente:

* **ERA5 — ECMWF Reanalysis v5**
* **IMERG — Integrated Multi-satellitE Retrievals for GPM**
* **ATMOS-BUD — ferramenta para diagnóstico de balanços atmosféricos**
* **GrADS — Grid Analysis and Display System**

Esses dados e ferramentas são utilizados para investigar a estrutura, trajetória e evolução de diferentes sistemas atmosféricos e seus processos físicos associados.

---

# 🎯 Objetivo do material

Mais do que simplesmente executar códigos ou gerar figuras, a proposta destes materiais é ajudar os estudantes a relacionar os conceitos discutidos em sala de aula com **dados atmosféricos reais e ferramentas utilizadas em pesquisa meteorológica**.

Recomenda-se observar, durante as atividades:

* quais variáveis meteorológicas estão sendo analisadas;
* em quais níveis atmosféricos os processos ocorrem;
* como identificar e acompanhar a trajetória de um ciclone;
* como o sistema evolui entre as fases incipiente, de intensificação, madura e de desintensificação;
* como os diferentes termos dos balanços atmosféricos contribuem para sua evolução;
* como interpretar diagramas de Hovmöller e perfis verticais;
* como a precipitação pode ser analisada em relação à climatologia;
* e como diferentes conjuntos de dados podem ser combinados em uma análise sinótica.

Os códigos podem ser modificados para explorar **outros eventos, períodos, regiões, níveis atmosféricos e sistemas meteorológicos**.

---

## 📚 IAG-USP — Ciências Atmosféricas

Material de apoio desenvolvido no contexto das atividades de **Meteorologia Sinótica III (ACA0524) — IAG/USP**.

**Monitor PAE:** Ronald Guiuseppi Ramírez Nina

**Contato:**

* [ronald.ramirez.nina@usp.br](mailto:ronald.ramirez.nina@usp.br)
* [ronald.ramirez.nina@alumni.usp.br](mailto:ronald.ramirez.nina@alumni.usp.br)
* [ronald.ramirez.nina@gmail.com](mailto:ronald.ramirez.nina@gmail.com)

