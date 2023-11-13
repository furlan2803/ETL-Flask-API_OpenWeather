# ETL com Flask + API

Criação de uma ETL em flask com teste de integração que leia da API OpenWeather, manipule os dados em uma tabela nova guardando as informações em 4 colunas: Data da Ingestão, Tipo, Valores, Uso.

## Introdução

Utilizando o framework Flask, o projeto desenvolve uma API que consome dados provenientes da API do OpenWeather, proporcionando informações climáticas globais para cidades ao redor do mundo. Além disso, o projeto inclui uma interface para visualização dos dados armazenados no banco de dados SQLite, bem como a implementação de testes para as funções aplicadas.

## Tecnologias

**OpenWeather:**

O OpenWeather é uma API que fornece dados climáticos em tempo real para diversas localidades ao redor do mundo. No projeto, essa tecnologia é utilizada para obter informações sobre as condições climáticas das cidades necessárias para análise e armazenamento.

**Python:**

Python é uma linguagem de programação versátil e de alto nível, amplamente usada no desenvolvimento de aplicativos e scripts. No projeto, Python é a linguagem principal, utilizada para a implementação de scripts de manipulação de dados, integração com a API OpenWeather e desenvolvimento da aplicação em Flask.

**Flask:**

Flask é um framework web em Python que simplifica o desenvolvimento de aplicativos web. No projeto, Flask é empregado para criar uma API simples que consome dados do OpenWeather e disponibiliza informações climáticas.

**HTML, CSS, JS:**

HTML (Hypertext Markup Language), CSS (Cascading Style Sheets) e JS (JavaScript) formam o trio para o desenvolvimento web. No projeto, HTML é utilizado para estruturar a interface, CSS para estilização e JS para interatividade.

**SQLite:**

SQLite é um sistema de gerenciamento de banco de dados leve, adequado para projetos menores. No contexto do projeto, SQLite é a escolha para armazenar e recuperar informações relacionadas às condições climáticas, proporcionando uma solução integrada e de fácil implementação para a persistência de dados.

## Estrutura do Projeto

```
Length Name
------ ----
-> __pycache__
-> .pytest_cache
-> instance
   -> etl_database.db
-> templates
   -> weather_table.html
   -> weather.html
-> api.py
-> README.md
-> requeriments.txt
-> test_api.py
```

O projeto é dividido em três partes principais:

- pytest_cache:

Diretório que armazena os dados de cache utilizados pelo framework de testes pytest.

- pycache:

Diretório que armazena arquivos de cache gerados automaticamente pelo interpretador Python para acelerar o processo de execução do código.

- instance:

Diretório que contém o arquivo etl_database.db. Este arquivo representa o banco de dados SQLite utilizado pelo projeto para armazenar informações climáticas.

- templates:

Diretório que contém os arquivos de template utilizados para renderizar páginas web. Os arquivos presentes são weather_table.html e weather.html.

- api.py:

Arquivo Python principal do projeto. Contém a lógica de implementação da API desenvolvida em Flask para consumir dados da API OpenWeather, processar esses dados e disponibilizá-los através de endpoints específicos.

- README.md:

Este arquivo, Markdown que fornece informações e documentação sobre o projeto, suas funcionalidades e como executá-lo.

- requirements.txt:

Arquivo que lista as dependências do projeto, ou seja, as bibliotecas e versões específicas do Python necessárias para a execução adequada do projeto.

- test_api.py:

Arquivo que contém os testes relacionados à API desenvolvida. Os testes validam se as funcionalidades da API estão funcionando conforme esperado.

## Arquivos principais

### API

O arquivo `api.py` contém as seguintes rotas:

- `/`: Rota principal da API que fornece um botão para visualização dos dados.
- `/weather_data`: Rota que retorna os dados climáticos armazenados no banco de dados.

### Testes

O arquivo `test_api.py` contém testes unitários para garantir que as funcionalidades principais do projeto estejam operacionais.

## Utilização

**Observação:**

Certifique-se de ter todas as dependências listadas no arquivo `requirements.txt` instaladas em seu computador antes de utilizar o projeto. 

### Executando a API

1. Clone este repositório em sua máquina.
2. No terminal, execute o seguinte comando:

```
python api.py
```

### Executando os Testes

1. No terminal, execute o seguinte comando:

```
pytest test_api.py
```

**Observação** :  É recomendável a utilização do terminal `WSL` para executar os testes.

## Resultados Esperados

Ao seguir as instruções de execução fornecidas acima, espera-se que o projeto seja inicializado com sucesso, tornando a API disponível para acesso. Além disso, ao executar os testes, os resultados esperados incluem a confirmação de que as funcionalidades principais do projeto estão operacionais, garantindo o correto funcionamento da aplicação.

### Resultados Esperados - API



### Resultados Esperados - Teste