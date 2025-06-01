import requests

# LOCAL
from .parametros import *
from .log import *

def api_post(url: str, conteudo={}, cabecalho={}):
    try:
        response = requests.post(url, data=conteudo, headers=cabecalho, verify=False)
        conteudo_token = response.json()
        return conteudo_token
    except:
        logger.error(f"Falha ao consumir API POST - URL: {url}")
        return False


def api_get(url: str, parametros={}, cabecalho={}):
    try:
        response = requests.get(url, headers=cabecalho, params=parametros, verify=False)
        conteudo_token = response.json()
        return conteudo_token
    except:
        logger.error(f"Falha ao consumir API POST - URL: {url}")
        return False