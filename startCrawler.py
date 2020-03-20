

import boto3
import argparse

parser = argparse.ArgumentParser(description='Script para iniciar um Crawler no AWS Glue')
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

response = client.start_crawler(Name=nameCrawler)

print (response)