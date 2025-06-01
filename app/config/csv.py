import csv

def escrever_linha_csv(arquivo:str, conteudo:list, codificacao:str="utf-8") -> bool:
    try:
        with open(arquivo, 'a+',  encoding=codificacao, newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(conteudo)
            return True
    except:
        return False

def carregar_csv(arquivo: str, delimitador:str):
    try:
        with open(arquivo, newline='', encoding='utf-8') as csvfile:
            conteudo = csv.reader(csvfile, delimiter=delimitador)
            return list(conteudo)
    except:
        return False