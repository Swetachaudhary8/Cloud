import boto
import boto.s3.connection

#prod
access_key = ''
secret_key = ''
d_host = '<Host_ip>'

conn = boto.connect_s3(
        aws_access_key_id = "<Access_Key>",
        aws_secret_access_key = "<Secret_Access_key>",
        host = d_host, 
    port = 80,
        is_secure=False,
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

bucket = conn.create_bucket('<Bucket_Name>')
