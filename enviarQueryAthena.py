import boto3
import argparse
import json
import time
import os.path

parser = argparse.ArgumentParser(description='Script para enviar uma query ao AWS Athena.')
parser.add_argument("--db", default=1, help="Database onde está a tabela no AWS Athena.")
parser.add_argument("--key", default=1, help="AWS Access Key usada para inicar a sessão.")
parser.add_argument("--saKey", default=1, help="AWS Secret Access Key usada para inicar a sessão.")
parser.add_argument("--reg", default=1, help="Região da AWS do onde o banco de dados do Athena está configurado.")

args = parser.parse_args()
athenaDataBase = args.db
AWS_ACCESS_KEY_ID = args.key
AWS_SECRET_ACCESS_KEY = args.saKey
AWS_DEFAULT_REGION = args.reg

#Variaveis de tempo
timeOut = 60 #segundos
cicloTimeOut = 60
contCicloTimeOut = 0

#lista de arquivos passada como parametro

fileNameList = ['<path1>', '<path2>']


totalArquivos = len(fileNameList)
contArquivos = 0
totalArquivosEncontrados = 0

outPutLocation = 's3://<path>'

client = boto3.client('athena',
                      aws_access_key_id = AWS_ACCESS_KEY_ID,
                      aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
                      region_name = AWS_DEFAULT_REGION)

queryAthena = 'SELECT ....'

print('Busca dos arquivos iniciada com sucesso!')

#Loop de espera dos arquivos
while contCicloTimeOut < cicloTimeOut:
    #Loop para pesquisar se os arquivos existem
    while contArquivos < totalArquivos:
        if os.path.isfile(fileNameList[contArquivos]):
            totalArquivosEncontrados = totalArquivosEncontrados + 1
        contArquivos = contArquivos + 1

    #Testa se os arquivos ainda não foram encontrados
    if totalArquivosEncontrados != totalArquivos:
        time.sleep(timeOut)
        contArquivos = 0
        totalArquivosEncontrados = 0
        contCicloTimeOut = contCicloTimeOut + 1
    #Se os arquivos forem encontrados, atribui as variaveis abaixo para sair do loop principal.
    else:
        contCicloTimeOut = cicloTimeOut


if totalArquivosEncontrados == totalArquivos:
    response = client.start_query_execution(QueryString=queryAthena,
                                            QueryExecutionContext={'Database':athenaDataBase},
                                            ResultConfiguration={'OutputLocation':outPutLocation}
                                            )
else:
    print("Total de arquivos nao encontrados!")


for pos in fileNameList:
    try:
        os.remove(pos)
    except FileNotFoundError as err:
        print(err)


filePath = '<path>'
fileNameTagAtlas = filePath + '<path>'
fileStatusCrawler = open(fileNameTagAtlas, 'w')
fileStatusCrawler.close()

filePath = '<path>'
fileNameTagAtlas = filePath + '<path>'
fileStatusCrawler = open(fileNameTagAtlas, 'w')
fileStatusCrawler.close()


print("Programa finalizado com sucesso!!")