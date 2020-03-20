import boto3
import argparse
import json
import time

timeOut = 60 #segundos
cicloTimeOut = 30
contCicloTimeOut = 0

filePath = '<path>'


parser = argparse.ArgumentParser(description='Script para consultar o status de um crawler do AWS Glue.')
parser.add_argument("--nc", default=1, help="Nome do Crawler no servico AWS Glue.")
parser.add_argument("--key", default=1, help="AWS Access Key usada para inicar a sessão.")
parser.add_argument("--saKey", default=1, help="AWS Secret Access Key usada para inicar a sessão.")
parser.add_argument("--reg", default=1, help="Região da AWS do onde o crawler está configurado.")

args = parser.parse_args()
nameCrawler = args.nc
AWS_ACCESS_KEY_ID = args.key
AWS_SECRET_ACCESS_KEY = args.saKey
AWS_DEFAULT_REGION = args.reg

client = boto3.client('glue',
                      aws_access_key_id = AWS_ACCESS_KEY_ID,
                      aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
                      region_name = AWS_DEFAULT_REGION)

response = client.get_crawler(Name=nameCrawler)
#pega o status atual do crawler
statusCrawler = response['Crawler']['State']

tempoEsperaStartCrawler = 15 #segundos
time.sleep(tempoEsperaStartCrawler)

print('Crawler {nameCrawler} iniciado!!')

while statusCrawler != 'READY' and contCicloTimeOut < cicloTimeOut:
    #faz a requisição para a AWS com o nome do crawler como parâmetro.
    response = client.get_crawler(Name=nameCrawler)
    #espera 1 minuto para encontrar o proximo status do crawler.
    time.sleep(timeOut)
    #pega o novo status do crawler após o tempo de espera do time out.
    statusCrawler = response['Crawler']['State']
    #incrementa em mais uma unidade a variável do ciclo do time out
    contCicloTimeOut = contCicloTimeOut + 1


if statusCrawler == 'READY' and contCicloTimeOut < cicloTimeOut:
    fileName = filePath+'/'+nameCrawler+'_READY'
    fileStatusCrawler = open(fileName,'w')
    fileStatusCrawler.close()

    fileNameTagAtlas = filePath + '/' + nameCrawler + '_READY_MARCACAO'
    fileStatusCrawler = open(fileNameTagAtlas, 'w')
    fileStatusCrawler.close()
else:
    print('Tempo de espera da execução do Crawler esgotado!!')

print('Programa finalizado com sucesso!!')
