# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:52:31 2019

@author: tiago.santos
"""

import boto3

awsAccessKeyId= ''
awsSecretAccessKey= ''
regionName= 'us-east-1'
roleARN= ''
clusterName= ''
serviceName= ''

ecsClient = boto3.client('ecs', 
                        aws_access_key_id= awsAccessKeyId,
                        aws_secret_access_key= awsSecretAccessKey,
                        region_name= regionName)

try:
    ecsClient.delete_service(cluster= clusterName,
                             service= serviceName,
                             force= True
                             )
except:
    print('Serviço já deletado.')

    
try:
   ecsClient.delete_cluster(cluster= clusterName)  

except:
    print('Cluster já deletado.')   
    
    
    
