# LIB
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
# LOCAL
from .parametros import *
from .log import *

# INICIALIZAÇÃO DO CHROME - SELENIUM
logger.info("Inicializando Selenium")
chrome_options = Options()
if AMBIENTE == "prod":
    chrome_options.add_argument("--headless")  # Rodar sem interface gráfica
    chrome_options.add_argument("--no-sandbox")  # Requerido em containers
    chrome_options.add_argument("--disable-dev-shm-usage")  # Evita problemas de memória
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
logger.success("Sucesso na inicialização do Selenium")

# FUNÇÕES PARA SIMPLIFICAR O CHROME - SELENIUM 

def buscar_elemento(xpath: str, tempo:int=TEMPO_ESPERA):
    driver.implicitly_wait(tempo)
    for n in range(tempo):
        try:
            return driver.find_element(By.XPATH, xpath)
        except:
            logger.info(f"Não achou o elemento: {xpath}. Iniciando nova tentativa.")
            sleep(1)
            continue
    return False

def abrir_site(site: str, tempo:int=TEMPO_ESPERA) -> bool:
    try:
        driver.get(site)
        driver.implicitly_wait(tempo)
        driver.minimize_window()
        driver.maximize_window()
        return True
    except:
        logger.critical("Falha ao abrir o site")
        return False

def selecionar_iframe(xpath:str) -> bool:
    try:
        driver.switch_to.default_content()
        iframe = buscar_elemento(driver, xpath)
        driver.switch_to.frame(iframe)
        return True
    except:
        logger.critical("Falha ao selecionar o elemento")
        return False
    
def escrever_no_elemento(xpath: str, texto: str) -> bool:
    try:    
        elemento = buscar_elemento(xpath)
        if(elemento != False):
            elemento.send_keys(texto)
            return True
    except:
        logger.error(f"Falha ao selecionar o elemento: {xpath}")
        return False

def clicar_no_elemento(xpath: str) -> bool:
    try:    
        elemento = buscar_elemento(xpath)
        if(elemento != False):
            elemento.click()
            return True
    except:
        logger.error(f"Falha ao selecionar o elemento: {xpath}")
        return False
    
def obter_valor_campo_selecao(xpath: str):
    try:    
        elemento = Select(buscar_elemento(xpath))
        return elemento.first_selected_option.text
    except:
        logger.error(f"Falha ao obter o valor do elemento: {xpath}")
        return False

def selecionar_campo_selecao_por_valor(xpath: str, texto: str) -> bool:
    try:    
        elemento = Select(buscar_elemento(xpath))
        elemento.select_by_value(texto)
        return True
    except:
        logger.error(f"Falha ao selecionar o campo de seleção - elemento: {xpath}")
        return False
    
def selecionar_campo_selecao_por_indice(xpath: str, indice: int) -> bool:
    try:    
        elemento = Select(buscar_elemento(xpath))
        elemento.select_by_index(indice)
        return True
    except:
        logger.error(f"Falha ao selecionar o campo de seleção - elemento: {xpath}")
        return False
    
def selecionar_campo_selecao_por_texto_visivel(xpath: str, texto: str) -> bool:
    try:    
        elemento = Select(buscar_elemento(xpath))
        elemento.select_by_visible_text(texto)
        return True
    except:
        logger.error(f"Falha ao selecionar o campo de seleção - elemento: {xpath}")
        return False

def mudar_janela_por_titulo(titulo:str) -> bool:
    e = False
    contador = 0
    while e == False:
        contador = contador + 1
        if contador == 10:
            logger.error(f"Falha ao encontrar a janela {titulo}")
            return False
        janelas = driver.window_handles
        for janela in janelas:
            driver.switch_to.window(janela)
            if driver.title == titulo:
                return  True
        sleep(1)

def fechar_janela_por_titulo(titulo:str) -> bool:
    e = False
    contador = 0
    while e == False:
        contador = contador + 1
        if contador == 10:
            logger.error(f"Falha ao encontrar a janela {titulo}")
            return False
        janelas = driver.window_handles
        for janela in janelas:
            driver.switch_to.window(janela)
            if driver.title == titulo:
                driver.close()
                driver.switch_to.window()
                return  True
        sleep(1)
