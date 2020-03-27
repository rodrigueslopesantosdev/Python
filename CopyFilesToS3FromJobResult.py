import boto3

awsAccessKey = ''
awsSecretAccessKey = ''
awsRegion = ''
athenaDataBase = ''
athenaQuery = ''
outPutLocation = ''

ciclosTimeOut = 1000;

athenaClient = boto3.client('athena',
                    aws_access_key_id=awsAccessKey,
                    aws_secret_access_key=awsSecretAccessKey,
                    region_name=awsRegion)

resultResponse = athenaClient.start_query_execution(QueryString=athenaQuery,
                                                    QueryExecutionContext={'Database': athenaDataBase},
                                                    ResultConfiguration={'OutputLocation': outPutLocation}
                                                    )

queryExecutionId = str(resultResponse["QueryExecutionId"])
resultResponse = athenaClient.get_query_execution(QueryExecutionId=queryExecutionId)

timeOut = 0
anoCompetencia=0
mesCompetencia=0

while (resultResponse["QueryExecution"]["Status"]["State"] != "SUCCEEDED" and timeOut < ciclosTimeOut):
    resultResponse = athenaClient.get_query_execution(QueryExecutionId=queryExecutionId)
    timeOut = timeOut + 1

if (resultResponse["QueryExecution"]["Status"]["State"] == "SUCCEEDED" and timeOut != ciclosTimeOut):
    resultResponse = athenaClient.get_query_results(QueryExecutionId=queryExecutionId)
    anoCompetencia = resultResponse["ResultSet"]["Rows"][1]["Data"][0]["VarCharValue"]
    mesCompetencia = resultResponse["ResultSet"]["Rows"][1]["Data"][1]["VarCharValue"]

    print("Consulta executada com sucesso!!")

    s3BucketName = ''
    newDirectory = "path"+'/ANO=' + str(anoCompetencia) + '/MES=' + str(mesCompetencia)
    s3 = boto3.client('s3',
                      aws_access_key_id=awsAccessKey,
                      aws_secret_access_key=awsSecretAccessKey,
                      region_name=awsRegion)

    s3.put_object(Bucket=s3BucketName, Key=(newDirectory + '/'))

    resourceS3 = boto3.resource('s3',
                                aws_access_key_id=awsAccessKey,
                                aws_secret_access_key=awsSecretAccessKey,
                                region_name=awsRegion)

    targetBucketName = ''
    targetPrefix = newDirectory + "/"

    sourceBucketName = ''
    sourcePrefix = ''

    bucketResource = resourceS3.Bucket(sourceBucketName)

    for obj in bucketResource.objects.filter(Prefix=sourcePrefix):
        copy_source = {
            'Bucket': sourceBucketName,
            'Key': obj.key
        }
        fileParquet = obj.key[len(sourcePrefix):len(obj.key)]
        resourceS3.meta.client.copy(copy_source, targetBucketName, (targetPrefix + str(fileParquet)))
        print('{0}:{1}'.format(bucketResource.name, obj.key))
        s3.delete_object(Bucket=sourceBucketName,
                         Key=obj.key)

    athenaDataBase = ''
    athenaQuery = ''
    resultResponse = athenaClient.start_query_execution(QueryString=athenaQuery,
                                                        QueryExecutionContext={'Database': athenaDataBase},
                                                        ResultConfiguration={'OutputLocation': outPutLocation}
                                                        )

else:
    print("Timeout da consulta!!")
    resultResponse = athenaClient.stop_query_execution(QueryExecutionId=queryExecutionId)