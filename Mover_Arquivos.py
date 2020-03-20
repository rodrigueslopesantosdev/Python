import boto3

"""Objeto para conectar ao AWS S3."""
s3_conexao = boto3.resource('s3')

"""Local de origem do arquivo"""
local_origem = {
        'Bucket': 'metadados',
        'Key' : 'Desenho PoC.jpg'        
        }

"""Local de destino do arquivo"""
local_destino = {
            'Bucket':'<bucker_name>',
        }

"""Chamada de função para copiar o arquivo de um bucket para outro."""
s3_conexao.meta.client.copy(local_origem, local_destino['Bucket'], local_origem['Key'])
"""Chamada de função para deletar o arquivo na origem que foi copiado."""
s3_conexao.Object(local_origem['Bucket'], local_origem['Key']).delete()