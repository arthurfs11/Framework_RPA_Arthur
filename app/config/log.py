from loguru import logger
from random import randint

ARQUIVO_LOG = "log.txt"
IDENTIFICACAO = randint(10,100000000)

logger.add(ARQUIVO_LOG, format="{time:DD/MM/YYYY HH:mm:ss} | {level} | {extra[id]} | {message}")
logger = logger.bind(id=IDENTIFICACAO)