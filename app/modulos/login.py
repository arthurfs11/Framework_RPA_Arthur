from config.selenium import *
from config.log import *
from config.parametros import *
from .elementos.login import *

def login_site():
    try:
        logger.info(f"Abertura do site: {SITE}")
        navegador = abrir_site(SITE)
        if(navegador == False):
            return False

        logger.info(f"Seleção campo de busca")
        acao_campo_busca = escrever_no_elemento(input_campo_busca, "Teste de velocidade")
        if(acao_campo_busca == False):
            logger.critical("Elemento de busca não encotrado essencial para execução do processo.")
            return False
        sleep(3)

        logger.info(f"Botão buscar")
        acao_botao_buscar = clicar_no_elemento(botao_buscar)
        if(acao_botao_buscar == False):
            logger.critical("Elemento do botão não encotrado essencial para execução do processo.")
            return False
        sleep(3)

        return True
    except Exception as error:
        logger.exception(error)

