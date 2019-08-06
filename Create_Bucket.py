# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:42:18 2019

@author: tiago.santos
"""

import boto3;
import logging;
from botocore.exceptions import ClientError;

"""Objeto para conectar ao AWS S3."""
s3_cliente = boto3.client('s3')
"""Chamada de função para criar o Bucket d580-teste"""
s3_cliente.create_bucket(Bucket='d580-teste')