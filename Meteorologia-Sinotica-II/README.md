# 🌎 Meteorologia Sinótica II — IAG/USP

**Materiais computacionais de apoio à disciplina Meteorologia Sinótica II (ACA0523)**, do Instituto de Astronomia, Geofísica e Ciências Atmosféricas da Universidade de São Paulo (**IAG/USP**).

Este diretório reúne notebooks em **Python/Jupyter** voltados à construção de cartas sinóticas, ao diagnóstico de sistemas atmosféricos e à interpretação física de dados meteorológicos. Os materiais foram organizados no contexto das atividades de monitoria do **Programa de Aperfeiçoamento de Ensino (PAE)**, com preferência pela execução no **Google Colab**.

> **Aviso:** estes materiais são complementares às aulas e não substituem as orientações ou os conteúdos oficiais da disciplina. Os notebooks podem depender da disponibilidade de dados externos, da data selecionada e das versões das bibliotecas Python.

## 🚀 Comece por aqui

Para executar um notebook **sem instalar Python no computador**:

1. Escolha um dos notebooks na tabela abaixo e clique em **Abrir no Colab**.
2. Faça login em uma conta Google, caso seja solicitado.
3. No Colab, selecione **Arquivo → Salvar uma cópia no Drive** para trabalhar sem modificar o arquivo original.
4. Leia as instruções do notebook e execute as células **na ordem**, começando pelas de preparação e instalação de dependências.
5. Ajuste datas, região, níveis de pressão e demais parâmetros de acordo com o exercício proposto.

**Alternativa:** acesse [Google Colab](https://colab.research.google.com/), escolha **Arquivo → Abrir notebook → GitHub** e informe o endereço do notebook no repositório.

> Alguns códigos fazem downloads de dados ou exigem configuração de bibliotecas. O tempo de execução, o consumo de memória e a possibilidade de obter os arquivos dependem do notebook e do ambiente utilizado.

## 📂 Notebooks e materiais disponíveis

| Tema | Arquivo | Objetivo | Execução |
| --- | --- | --- | --- |
| Análise isentrópica | [`Isentropic_charts_GFS_analysis.ipynb`](Isentropic_charts_GFS_analysis.ipynb) | Gerar cartas em superfícies isentrópicas (310, 330 e 350 K), examinando pressão, vento e vorticidade potencial, além de diagnósticos relacionados às esteiras transportadoras (*conveyor belts*). | [Abrir no Colab](https://colab.research.google.com/github/RonaldRN/Monitorias_IAG-USP/blob/main/Meteorologia-Sinotica-II/Isentropic_charts_GFS_analysis.ipynb) |
| Jatos em altos níveis | [`JET_POLAR_SUBTROPICAL.ipynb`](JET_POLAR_SUBTROPICAL.ipynb) | Construir cartas para identificação e análise do Jato Polar (JP) e do Jato Subtropical (JST). | [Abrir no Colab](https://colab.research.google.com/github/RonaldRN/Monitorias_IAG-USP/blob/main/Meteorologia-Sinotica-II/JET_POLAR_SUBTROPICAL.ipynb) |
| Cartas sinóticas com ERA5 | [`Synoptic_chart_Reanalysis_ERA5.ipynb`](Synoptic_chart_Reanalysis_ERA5.ipynb) | Visualizar e combinar campos atmosféricos da reanálise ERA5 para análise sinótica. | [Abrir no Colab](https://colab.research.google.com/github/RonaldRN/Monitorias_IAG-USP/blob/main/Meteorologia-Sinotica-II/Synoptic_chart_Reanalysis_ERA5.ipynb) |
| Cartas sinóticas com GFS — Parte I | [`Synoptic_charts_GFS_analysis_Part_I.ipynb`](Synoptic_charts_GFS_analysis_Part_I.ipynb) | Introduzir campos meteorológicos e combinações de variáveis utilizadas na análise sinótica do GFS. | [Abrir no Colab](https://colab.research.google.com/github/RonaldRN/Monitorias_IAG-USP/blob/main/Meteorologia-Sinotica-II/Synoptic_charts_GFS_analysis_Part_I.ipynb) |
| Cartas sinóticas com GFS — Parte II | [`Synoptic_charts_GFS_analysis_Part_II.ipynb`](Synoptic_charts_GFS_analysis_Part_II.ipynb) | Ampliar os diagnósticos da Parte I com cartas e combinações adicionais de campos atmosféricos. | [Abrir no Colab](https://colab.research.google.com/github/RonaldRN/Monitorias_IAG-USP/blob/main/Meteorologia-Sinotica-II/Synoptic_charts_GFS_analysis_Part_II.ipynb) |
| Estrutura vertical de altas e baixas | [`Synoptic_charts_identification_High_Low_pressure_systems_GFS_analysis.ipynb`](Synoptic_charts_identification_High_Low_pressure_systems_GFS_analysis.ipynb) | Explorar interativamente a estrutura vertical de centros de alta e baixa pressão com mapas de superfície e níveis isobáricos. | [Abrir no Colab](https://colab.research.google.com/github/RonaldRN/Monitorias_IAG-USP/blob/main/Meteorologia-Sinotica-II/Synoptic_charts_identification_High_Low_pressure_systems_GFS_analysis.ipynb) |
| Zona de Convergência Intertropical | [`ZCIT_GOES19_GFS.ipynb`](ZCIT_GOES19_GFS.ipynb) | Integrar imagens do GOES-19 e campos do GFS para analisar a Zona de Convergência Intertropical (ZCIT). | [Abrir no Colab](https://colab.research.google.com/github/RonaldRN/Monitorias_IAG-USP/blob/main/Meteorologia-Sinotica-II/ZCIT_GOES19_GFS.ipynb) |
| Jato de Baixos Níveis da América do Sul | [`IDENTIFICATION_SALLJ.ipynb`](IDENTIFICATION_SALLJ.ipynb) | Aplicar e visualizar critérios de identificação do *South American Low-Level Jet* (SALLJ) e examinar a circulação de baixos níveis. | [Abrir no Colab](https://colab.research.google.com/github/RonaldRN/Monitorias_IAG-USP/blob/main/Meteorologia-Sinotica-II/IDENTIFICATION_SALLJ.ipynb) |
| Funções auxiliares | [`utilities_new_version.py`](utilities_new_version.py) | Reunir rotinas de apoio, incluindo processamento de dados do GOES-19 e operações com coordenadas e reprojeções. | [Ver código](utilities_new_version.py) |

## 🧭 Conteúdos abordados

### Cartas sinóticas e análise tridimensional

Os notebooks das Partes I e II do GFS e o notebook de ERA5 permitem relacionar a distribuição espacial dos campos atmosféricos com a estrutura e a evolução de sistemas sinóticos. Ao executar os códigos, procure identificar **quais variáveis e níveis** estão representados, a relação entre os campos e os mecanismos físicos associados aos padrões observados.

### Superfícies isentrópicas

A análise das superfícies de **310, 330 e 350 K** permite examinar a circulação em superfícies de temperatura potencial constante. O notebook apresenta diagnósticos de pressão, vento e **vorticidade potencial**, com resultados em unidades de vorticidade potencial (*PVU*), e produtos para investigar estruturas associadas ao transporte atmosférico e às esteiras transportadoras (*conveyor belts*).

### Jato Polar, Jato Subtropical e SALLJ

O notebook `JET_POLAR_SUBTROPICAL.ipynb` é destinado à análise dos jatos de altos níveis. Já `IDENTIFICATION_SALLJ.ipynb` aborda a **identificação do Jato de Baixos Níveis da América do Sul (SALLJ)**. Ao utilizar este último, é importante diferenciar a presença de ventos intensos em baixos níveis da **satisfação dos critérios específicos de identificação** implementados no código. Consulte as células do notebook para verificar os parâmetros e limiares adotados.

O SALLJ tem relevância para o transporte de umidade e a organização de sistemas meteorológicos na América do Sul. A interpretação dos mapas deve considerar a localização e a intensidade dos ventos, a estrutura vertical e o contexto sinótico.

### Estrutura vertical de altas e baixas pressões

O notebook interativo combina a **pressão reduzida ao nível médio do mar** com alturas geopotenciais em **850, 700 e 500 hPa**. A visualização produzida com **Plotly/Dash** permite selecionar uma região de interesse no mapa de superfície e compará-la com os níveis superiores. O exercício ajuda a investigar o alinhamento ou a inclinação vertical dos sistemas e a discutir sua estrutura térmica.

> No Colab, a visualização Dash pode depender da versão instalada; o exemplo existente utiliza a execução do aplicativo no próprio notebook.

### Zona de Convergência Intertropical

O notebook `ZCIT_GOES19_GFS.ipynb` combina produtos de satélite **GOES-19** e campos do **GFS**, auxiliando na identificação de padrões de nebulosidade e circulação associados à ZCIT. A interpretação deve considerar tanto a informação de satélite quanto os campos atmosféricos analisados.

## 🛰️ Fontes de dados

Os materiais utilizam, conforme o notebook:

- **GFS — Global Forecast System:** campos de análise meteorológica em diferentes níveis.
- **ERA5 — ECMWF Reanalysis v5:** campos de reanálise para diagnóstico atmosférico.
- **GOES-19:** dados de observação por satélite utilizados em produtos meteorológicos.

Os downloads podem ser realizados a partir de fontes externas, e algumas rotinas relacionadas ao GOES-19 utilizam serviços públicos da Amazon Web Services (AWS). **A execução não garante que todo arquivo histórico ou data selecionada esteja disponível**. Quando um dado não puder ser obtido, confira a data, a fonte consultada e as mensagens de erro do notebook.

## 🐍 Bibliotecas e ambiente Python

As dependências variam por notebook. Entre as bibliotecas utilizadas nos materiais estão `numpy`, `xarray`, `pandas`, `matplotlib`, `cartopy`, `cmocean`, `netCDF4`, `MetPy`, `SciPy`, `requests`, `boto3`, `pygrib`, `cfgrib`, `GDAL`, `Shapely`, `Plotly`, `Dash` e `Kaleido`.

**No Google Colab:** execute inicialmente as células de preparação do notebook escolhido. Não é necessário instalar todos os pacotes da lista para trabalhar com um único arquivo.

**Na execução local:** recomenda-se um ambiente Python isolado e o uso de JupyterLab ou Jupyter Notebook. Dependências como `GDAL`, `pygrib`, `cfgrib`/`ecCodes` podem exigir instalações adicionais específicas do sistema operacional. A exportação de figuras do Plotly para imagens estáticas pode requerer `Kaleido` compatível com a versão do Plotly instalada.

## 💻 Como baixar e executar localmente

### Opção 1 — Clonar com Git

```bash
git clone https://github.com/RonaldRN/Monitorias_IAG-USP.git
cd Monitorias_IAG-USP/Meteorologia-Sinotica-II
```

Com Jupyter já instalado no seu ambiente Python:

```bash
jupyter lab
```

Ou, caso utilize a interface clássica:

```bash
jupyter notebook
```

Selecione o arquivo `.ipynb` desejado. Se alguma biblioteca estiver ausente, siga as orientações do próprio notebook e do ambiente Python utilizado.

### Opção 2 — Baixar o arquivo ZIP

1. Acesse a [página principal do repositório](https://github.com/RonaldRN/Monitorias_IAG-USP).
2. Clique em **Code → Download ZIP**.
3. Extraia o arquivo e abra a pasta `Monitorias_IAG-USP/Meteorologia-Sinotica-II/`.
4. Execute o notebook usando um ambiente Jupyter compatível ou envie-o ao Google Colab.

### Atualizar uma cópia clonada

Na pasta principal do repositório, execute:

```bash
git pull origin main
```

> Caso existam alterações locais não salvas ou commits ainda não integrados, resolva-os antes de atualizar o repositório.

## 🎯 Sugestões para as atividades da monitoria

Além de gerar as cartas meteorológicas, recomenda-se:

1. **Identificar** as variáveis, unidades, níveis atmosféricos e horários utilizados.
2. **Comparar** padrões em superfície, baixos níveis e altos níveis, quando aplicável.
3. **Relacionar** os resultados com os conceitos de dinâmica atmosférica apresentados na disciplina.
4. **Avaliar** como a interpretação muda com a data, a região ou os níveis selecionados.
5. **Registrar** limitações relacionadas à resolução espacial, à disponibilidade de dados e aos critérios de identificação dos sistemas.

Os códigos são ferramentas didáticas e podem ser adaptados a outras situações sinóticas, desde que as alterações sejam verificadas e interpretadas fisicamente.

## 📚 Créditos e referências

O estilo de algumas cartas dos notebooks `Isentropic_charts_GFS_analysis.ipynb` e `Synoptic_charts_GFS_analysis_Part_II.ipynb` foi inspirado nos produtos de diagnóstico sinótico do **[GFS Archive de Alicia M. Bentley](https://www.atmos.albany.edu/student/abentley/realtime/archive.php)**.

Essa referência diz respeito à inspiração **conceitual e visual**; não implica que os códigos deste repositório integrem o GFS Archive original. Os materiais foram desenvolvidos ou adaptados para fins didáticos no contexto da monitoria de Meteorologia Sinótica II.

## 👨‍💻 Monitor PAE e contato

**Ronald Guiuseppi Ramírez Nina**  
Doutorando em Ciências Atmosféricas — IAG/USP  
Monitor/Estagiário PAE — Meteorologia Sinótica II

- **E-mail institucional:** [ronald.ramirez.nina@usp.br](mailto:ronald.ramirez.nina@usp.br)
- **E-mail alternativo:** [ronald.ramirez.nina@alumni.usp.br](mailto:ronald.ramirez.nina@alumni.usp.br)
- **E-mail pessoal:** [ronald.ramirez.nina@gmail.com](mailto:ronald.ramirez.nina@gmail.com)
- **GitHub:** [@RonaldRN](https://github.com/RonaldRN)

Dúvidas sobre a execução dos notebooks, interpretação dos produtos ou funcionamento dos códigos podem ser encaminhadas pelos contatos acima.
