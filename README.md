# Nome do Bot

## 1 - Sobre
descricao breve sobre a funcionalidade do bot

## 2 - Tecnologias Utilizadas
As tecnologias utilzadas no processo foram:
- Python
- Selenium
- Requests
- Loguru
- ChromeDriverManager

## 3 - Instalação
Requer python 3.9 e Google Chrome instalados.

## 4 - Configurações
As configurações estão parametrizadas no arquivo `app/config/parametros.py`.

### 4.1 - Ambiente
A mudanca de ambiente é configurada na variavel de ambiente chamada `AMBIENTE` que pode ter os valores `dev` ou `prod`.

### 4.2 - Site
A variável aponta para o site que irá iniciar a execução do processo

### 4.3 - Tempo de espera
Tempo de espera padrão nas atividades realizadas no Chrome Driver.

## Organização das pastas
- app
    - config
        - api.py #contém as funções personalizadas relacionadas a API.
        - csv.py  #contém as funções personalizadas relacionadas a CSV.
        - data.py  #contém as funções personalizadas relacionadas a Datas.
        - log.py  #contém as funções personalizadas relacionadas aos LOGs.
        - parametros.py  #contém as funções personalizadas relacionadas aos Parametros.
        - selenium.py   #contém as funções personalizadas relacionadas ao Selenium.
    - modulos
        - qualquer_arquivo.py   #cada arquivo nessa pasta representa uma task do robô.
    - main.py #ponto de partida inicial que contém o fluxo de execução dos módulos.
- motor
    - Scripts
        - activate #responsável por ativar o ambiente virtual, necessário para isolar os códigos/robôs.
- Dockerfile # arquivo de configurações do Docker
- log.txt  # arquivo gerado resultado de uma execução.
- requirements.txt # Libs necessárias para execução.

## 6 - Execução
Primeiro a ativação do ambiente de virtual.
```ssh
motor/Scripts/activate
```

Após a execução do script.
```ssh
py app/main.py
```