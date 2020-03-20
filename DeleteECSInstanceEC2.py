

import boto3

awsAccessKeyId= ''
awsSecretAccessKey= ''
regionName= ''
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
    
    
    
