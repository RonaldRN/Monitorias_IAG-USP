# Monitoria-Meteorologia-Sinotica-IAG-USP
Repositorio dos códigos feitos em Google Colab de programação em Python de arquivos com extensão .ipynb

Autor: MSc. Student Ronald Guiuseppi Ramírez Nina 

Professora da disciplina: Rita Yuri Ynoue

Este repositório contém os arquivos .ipynb das aulas práticas realizadas em python na disciplina de "Meteorología Sinótica I" 
no Instituto de Astronomia, Geofisica e Ciências Atmosférica - Universidade de São Paulo, São Paulo, Brazil. 

--------------------------------------------------------------------------------------------------------------------------------
# Aula_Pratica-1

O objetivo desta aula é fazer o seguinte (Aula_01.ipynb):
- Ler dados NetCDF do NCEP/NOAA 
- Fazer mapas dos campos meteorológicos utilizando o pacote "cartopy"
- Atividade de casa 

---------------------------------------------------------------------------------------------------------------------------------
# Aula_Pratica-2

O Objetivo desta aula é fazer o seguinte (Aula_02.ipynb):
- Utilizar o pacote HydroBr
- Acessar à base dados do INMET (Instituto Nacional de Meteorologia) com o HydroBr
- Visualizar a rede de estações automáticas por estado do Brasil. 
- Fazer o cálculo de médias e acumulados (precipitação) dos ciclos diurno, mensal e anual.
- Fazer gráficos dos ciclos médios diurnos, mensal e anual.
- Fazer estudos de caso para períodos específicos.
- Fazer um climograma para uma estação automática em específico.

Nota: O arquivo "Aula_02-DataFrame.ipynb" acessa a arquivos .csv e faz o mesmo que o código anterior.

----------------------------------------------------------------------------------------------------------------------------------
# Aula_Pratica-3

O objetivo desta aula é fazer o seguinte (Aula_03.ipynb):
- Utilizas os pacotes Siphon e MetPy.
- Acessar à base de dados das radiossondagens da University of Wyoming.
- Elaborar o diagrama Skew-T Log-P com os dados da radiossondagem.
- Adicionar ao diagrama Skew-T Log-P a hodógrafa e parâmetros termodinâmicos (index Showalter, index Lifted, e outros).

Nota: O arquivo "Aula_03-import-file-csv.ipynb.ipynb" acessar a arquivos .csv e faz o mesmo que o código anterior.

-----------------------------------------------------------------------------------------------------------------------------------
# Aula_Pratica-4

O objtivo desta aula é fazer o seguinte (Aula_04.ipynb):
- Utilizar o pacote MetPy para plotar os códigos METAR. 
- Utilizar os reportes METAR disponibilizados no seguinte link: https://thredds-test.unidata.ucar.edu/thredds/catalog/noaaport/text/metar/catalog.html
- Elaborar um mapa de América do Sul com os modelos de estação dos reportes METAR.

--------------------------------------------------------------------------------------------------------------------------------------
# Aula_Pratica-5

O objtivo desta aula é fazer o seguinte (Aula_05.ipynb)
- Utilizar o pacote pygrib.
- Ler dados grib do modelo global - Global Forecast System (GFS)
- Fazer um mapa da Pressão Reduzida ao Nível do Mar.

--------------------------------------------------------------------------------------------------------------------------------------
# Aula_Pratica-6

O objtivo desta aula é fazer o seguinte (Aula_06.ipynb)
- Utilizar o pacote pygrib, cartopy para fazer os mapas meteorológicos.
- Ler dados grib do modelo global - Global Forecast System (GFS)
- Fazer mapas do campo de altura geopotencial nos níveis de 850, 500 e 250 hPa.
- Reconhecer e trazar cristas e cavados.
- Plotar os campos de altura geopotencial e Jato no nível de 250 hpa.

--------------------------------------------------------------------------------------------------------------------------------------
# Aula_Pratica-7

O objtivo desta aula é fazer o seguinte (Aula_07.ipynb)
- Utilizar o pacote pygrib, cartopy e NetCDF4 para fazer os mapas meteorológicos.
- Fazer Download de imagens de satélite GOES-16 do repositoório do Amazon.
- Ler dados do satélite GOES-16 médiante o pacote NetCDF4. 
- Ler dados grib do modelo global - Global Forecast System (GFS)
- Fazer mapas utilizando a imagem de satélite do GOES-16 com dados do modelo GFS.
- Fazer o mapa da Banda 13 do Goes-16, Pressão Reduzida ao Nível Médio do Mar e Espessura entre 500-1000 hPa.
