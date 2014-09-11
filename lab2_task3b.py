import sys
import argparse
from collections import defaultdict

# Input parameter check
parser = argparse.ArgumentParser(description='E-mail parsing help')
parser.add_argument('infile',nargs="?",type=file,help="Input file")
try:
	args = parser.parse_args()
except Exception as e:
	parser.print_help(); print e

# Variables	
f=args.infile
words=defaultdict(int)

for line in f:
	for word in line.strip().split():
		words[word.lower().decode('utf-8')]+=1

maxlen=len( max( words, key=len))+1
maxval=max(words.values())
formatstr="%"+str(maxlen)+"s | %-20s | %d"

for word in words:
	dots=int(float(words[word])/maxval*20.0)
	print formatstr % (word,"@"*dots,words[word])
