from modulos.login import *
from modulos.intranet import *
import sys

# PRIMEIRA TASK
if(login_site()):
    logger.success("Primeira task realizada.")
else:
    logger.error("Encerrando processo na primeira task.")
    sys.exit()

# SEGUNDA TASK
if(navegacao_intranet()):
    logger.success("Segunda task realizada.")
else:
    logger.error("Encerrando processo na segunda task.")
    sys.exit()
    