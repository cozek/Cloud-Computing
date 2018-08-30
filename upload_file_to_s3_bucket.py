import boto3


s3 = boto3.client('s3') 


filename = 'just-a-file.txt'  #the file we are gonna upload to s3 bucket


bucket_name = 'kaushik-bucket-boto' #replace with your bucket name

s3.upload_file(filename,bucket_name,filename) #upload command

