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

fileNameList = ['/home/nifi/scripts/arquivosRespostaGlue/crw_cliente_pf_READY','/home/nifi/scripts/arquivosRespostaGlue/crw_faturas_pf_READY']


totalArquivos = len(fileNameList)
contArquivos = 0
totalArquivosEncontrados = 0

outPutLocation = 's3://aws-athena-query-results-944144161735-us-east-1'

client = boto3.client('athena',
                      aws_access_key_id = AWS_ACCESS_KEY_ID,
                      aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
                      region_name = AWS_DEFAULT_REGION)

queryAthena = 'insert into axxiom.cliente_fatura_pf \
select \
   cast(cd_fatura as integer) cd_fatura, \
   fat.cd_und_consumidor, \
   cast(fat.dt_leitura as date) dt_leitura, \
   cast(fat.dt_vencimento as date) dt_vencimento, \
   cast(fat.dt_pagamento as date) dt_pagamento, \
   cast(fat.vr_fatura as decimal(15,2)) vr_fatura, \
   cast(fat.qt_consumo_kwh as decimal(15,2)) qt_consumo_kwh, \
   cast(substring(fat.dt_atualizacao, 1, 10) as date) dt_atualizacao, \
   cli.nr_cpf, \
   cli.nm_nome, \
   cast(cli.nr_idade as integer) nr_idade, \
   cast(cli.dt_nascimento as date) dt_nascimento, \
   cli.ds_etnia, \
   cli.ds_religiao, \
   cli.ds_sexo, \
   cli.ds_nacionalidade, \
   cli.ds_naturalidade, \
   cli.ds_logradouro, \
   cli.ds_cidade, \
   cli.ds_uf, \
   cli.nr_cep, \
   cli.ds_estado_civil \
from axxiom.faturas_pf fat \
     join axxiom.cliente_pf cli \
         on fat.cd_cliente = cli.cd_cliente \
where not exists (select 1 FROM axxiom.cliente_fatura_pf pf \
                     where cli.nr_cpf = pf.nr_cpf \
                     and cast(fat.dt_pagamento as date) = pf.dt_pagamento)'

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


filePath = '/home/nifi/scripts/arquivosRespostaGlue'
fileNameTagAtlas = filePath + '/crw_faturas_pf_READY_MARCACAO'
fileStatusCrawler = open(fileNameTagAtlas, 'w')
fileStatusCrawler.close()

filePath = '/home/nifi/scripts/arquivosRespostaGlue'
fileNameTagAtlas = filePath + '/crw_cliente_pf_READY_MARCACAO'
fileStatusCrawler = open(fileNameTagAtlas, 'w')
fileStatusCrawler.close()


print("Programa finalizado com sucesso!!")