#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unicodedata
import codecs
import argparse
from unicodedata import normalize, category

parser = argparse.ArgumentParser(description='E-mail parsing help')
parser.add_argument('infile',nargs="?",type=file,help="Input file")


try:
	args = parser.parse_args()
except Exception as e:
	parser.print_help(); print e

if (args.infile == None):
	input_name=raw_input('Give your full name: ')
	separated_name=input_name.lower().strip().decode("utf8")
	s2=unicodedata.normalize('NFD',separated_name)
	#deacuted=''
	original_email_name=[]
	for c in s2:
		char_type=unicodedata.category(c)
		if char_type=='Ll' or char_type=="Nd":
			original_email_name.append(c)
	original_email_name.reverse()
	print(original_email_name)
	new_mail_name=".".join(original_email_name)
	print("%s@foobar.com" % new_mail_name)

else:
	f=args.infile
	original_email_name=[]
	for line in f:
		s2=line.strip().lower().decode("utf8")
		s3=unicodedata.normalize('NFD',s2)
		for c in s3:
			char_type=unicodedata.category(c)
			if char_type=='Ll' or char_type=="Nd":
				original_email_name.append(c)
			original_email_name.reverse()
		#print(original_email_name)
		new_mail_name=".".join(original_email_name)
		print("%s@foobar.com" % new_mail_name)
	
