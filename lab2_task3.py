#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import collections
from itertools import chain

parser = argparse.ArgumentParser(description='E-mail parsing help')
parser.add_argument('infile',nargs="?",type=file,help="Input file")

try:
	args = parser.parse_args()
except Exception as e:
	parser.print_help(); print e
	
f=args.infile
words={}

for line in f:
	for word in line.strip().split():
		word=word.lower().decode('utf-8')
		print(word)
	if(words.has_key(word)):
		words[word]+=1
	else:
		words[word]=1

for word in words:
	print"%10s | %-20s | %d" % (word,"@"*words[word],words[word])
