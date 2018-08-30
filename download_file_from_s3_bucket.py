import boto3

s3 = boto3.client('s3')

filename = 'my_file_name' #replace with your filename

bucket_name = 'kaushik-bucket-boto' #replace with your bucket name

s3.upload_file(filename,bucket_name,filename) 

