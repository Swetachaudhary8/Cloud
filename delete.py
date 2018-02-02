import os

import boto
from boto.s3.key import Key
import boto.s3.connection
#AWS Details
AWS_ACCESS_KEY = ' '
AWS_ACCESS_SECRET_KEY = ' '

conn = boto.connect_s3(AWS_ACCESS_KEY, AWS_ACCESS_SECRET_KEY, host = "<host_Ip>", port = 80,
        is_secure=False,              
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
)
bucket = conn.get_bucket("<Bucket Name> ", validate=True)
bucket.delete_key('home/sweta.chaudhary/tmp.log')
