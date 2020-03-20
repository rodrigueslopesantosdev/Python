import boto3

awsAccessKeyId= ''
awsSecretAccessKey= ''
regionName= ''

fireHoseDeliveryStreamName = 'kinesis-firehose'
kinesisDataStreamName= 'kinesis-dms'

firehose = boto3.client('firehose', 
                        aws_access_key_id= awsAccessKeyId,
                        aws_secret_access_key= awsSecretAccessKey,
                        region_name= regionName)

kinesis = boto3.client('kinesis', 
                        aws_access_key_id= awsAccessKeyId,
                        aws_secret_access_key= awsSecretAccessKey,
                        region_name= regionName)

try:
    firehoseResponse = firehose.delete_delivery_stream(DeliveryStreamName = fireHoseDeliveryStreamName)
except:
    print('Firehose Delivery Stream já foi deletado.')

try:
    kinesisResponse = kinesis .delete_stream(StreamName = kinesisDataStreamName)
except:
    print('Kinesis Data Stream já foi deletado.')