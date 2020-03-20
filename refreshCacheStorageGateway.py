
import argparse
import boto3

parser = argparse.ArgumentParser(description='Script para iniciar o Refresh Cache do AWS Storage Gateway.')
parser.add_argument("--key", default=1, help="AWS Access Key usada para inicar a sessão.")
parser.add_argument("--saKey", default=1, help="AWS Secret Access Key usada para inicar a sessão.")
parser.add_argument("--reg", default=1, help="Região da AWS onde o Storage Gateway está configurado.")

args = parser.parse_args()
AWS_ACCESS_KEY_ID = args.key
AWS_SECRET_ACCESS_KEY = args.saKey
AWS_DEFAULT_REGION = args.reg

"""Objeto para conectar ao AWS S3."""
clientStorageGateway = boto3.client('storagegateway',
                                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                    region_name=AWS_DEFAULT_REGION)


resposta = clientStorageGateway.list_gateways()

gatewayARN = resposta['Gateways'][0]['GatewayARN']

print(resposta['Gateways'][0]['GatewayARN'])

resposta = clientStorageGateway.list_file_shares(
        GatewayARN=gatewayARN)

fileShareARN = resposta['FileShareInfoList'][0]['FileShareARN']

resposta = clientStorageGateway.refresh_cache(FileShareARN=fileShareARN,
                                              FolderList=['/'],
                                              Recursive=True)

print (resposta)
