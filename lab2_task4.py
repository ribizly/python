import sys
import argparse
import operator
from collections import defaultdict

# Input parameter check
parser = argparse.ArgumentParser(description='E-mail parsing help')
parser.add_argument('-t','--top',nargs='*',help="With a value, that specifies the top N values to be printed")
parser.add_argument('infile',nargs="?",type=file,help="Input file")
args=None
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

l=[(x,words[x]) for x in words.keys()]
print(max(l[2]))
sortedl=sorted(l, key=operator.itemgetter(1), reverse=True)
print(sortedl)

for word in sortedl:
	dots=int(float(word[1])/maxval*20.0)
	print formatstr % (word[0],"@"*dots,word[1])
