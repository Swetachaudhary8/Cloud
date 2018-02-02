import os
import time
import boto
from boto.s3.key import Key
import boto.s3.connection


#file details
cur_date = (time.strftime("%d-%m-%Y"))
consumption = "consumption_" + cur_date + ".csv"

#AWS Details
AWS_ACCESS_KEY = '<Accesskey> '
AWS_ACCESS_SECRET_KEY = '<accesssecretkey>'
#file_name = ("tmps.log")
path = "/grid/1/consumption/"
file = os.path.join(path, consumption)
f = open(file, 'r+')
conn = boto.connect_s3(AWS_ACCESS_KEY, AWS_ACCESS_SECRET_KEY, host = "10.47.2.2", port = 80,
        is_secure=False,              
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
)
b = conn.get_bucket("Bucket_Name")
k = Key(b)
k.key = consumption
k.set_contents_from_file(f)
