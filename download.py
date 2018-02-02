#!/usr/bin/python

import os
import sys, getopt
import boto
from boto.s3.key import Key
import boto.s3.connection


def main(argv):
	inputkey = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv, "hi:o:", ["ifile=","ofile="])
	except getopt.GetoptError as err:
		print 'download.py -i <inputdate> -o <outputfile>'
		print str(err)
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print "download.py -i <inputdate> -o <outputfile>"
			print "please provide correct input date in format(dd-mm-yyyy)and output file name with path"
			sys.exit()			
		elif opt in ('-i',"--ifile"):
			inputkey = arg
		elif opt in ('-o',"--ofile"):
			outputfile = arg
		
	inputfile = "consumption_"  + inputkey + ".csv"
 	i = "'"+ inputfile+ "'"
	o = "'"+ outputfile + "'"
	#AWS Details
        AWS_ACCESS_KEY = '<Please give access Key>'
        AWS_ACCESS_SECRET_KEY = '<Please give Secret key>'

        #s3 connections
        conn = boto.connect_s3(AWS_ACCESS_KEY, AWS_ACCESS_SECRET_KEY, host = "<Host_ip>", port = 80,   
        is_secure=False,
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
)       
        bucket = conn.get_bucket("<BuckeT_Name>", validate=True)
	print "Connecting  storage ......................................................"
        key = bucket.get_key(inputfile)
	print "..................................Downloading files..............................."
        key.get_contents_to_filename(outputfile)
	print "File download at path %s" % (outputfile)
	print "DOWNLOAD COMPLETED"

if __name__ == "__main__":
   main(sys.argv[1:])
