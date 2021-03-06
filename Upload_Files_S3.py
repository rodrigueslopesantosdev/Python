
import boto3;
import logging;
from botocore.exceptions import ClientError;

"""Função definida para envio de arquivos ao AWS S3"""
def envia_arquivo (nome_arquivo, bucket, nome_objeto=None):
    """Se o nome do objeto for vazio, então o nome do objeto será igual ao do arquivo."""    
    if nome_objeto is None:
        nome_objeto=nome_arquivo
        
    """Objeto para conectar ao AWS S3."""
    s3_conexao = boto3.client('s3')
    
    """Try catch para tentar o upload do arquivo."""
    try:
        resposta = s3_conexao.upload_file(nome_arquivo, bucket, nome_objeto)
    """Exception caso a tentativa de conexão aconteça sem sucesso."""    
    except ClienteError as erroMensagem:
            logging.error(erroMensagem)
            return False
    return True

"""Variável com o nome do arquivo para upload."""        
nome_arquivo = '<FILE PATH>'

print ('Programa iniciado!')
print ('Enviando arquivo!')

"""Chamada da função de envio do arquivo para a AWS S3."""
envia_arquivo(nome_arquivo, '<bucket_s3>', '<nome_arquivo>')

print ('Arquivo enviado!')
print ('Programa terminado com sucesso!')