import boto3
import time
from pprint import pprint

ec2 = boto3.resource('ec2')

# below is an user script that installs apache server in our launched instance and replace the apache default page
# with an static html page hosted somewhere on the internet. lol.

user_data_script ="""#!/bin/bash
sudo apt-get update
sudo apt-get install -y build-essential
sudo apt-get install -y apache2
curl "link to your html webpage, insert here" > index.html
sudo rm /var/www/html/index.html
sudo mv index.html /var/www/html/index.html"""


ec2.create_instances(
    ImageId='ami-759bc50a', #replace with the ami id of your choice
    MinCount=1,
    MaxCount=1,
    KeyName="ec2-1", #replace with your key-pair name
    UserData=user_data_script, 
    SecurityGroups=["http_security_group"], #security group should have port 80 open and allow TCP traffic
    InstanceType='t2.micro' 
    )


time.sleep(50) #sleep a while before retreiving instance information else you might not get the desired response.

# filters the intances by "running" instances. and displays its information. Read the boto 3 docs for more info on this. 
# If you open the public dns in your browser your should be seeing your webpage hosted.

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id, instance.instance_type,instance.public_dns_name)
    



