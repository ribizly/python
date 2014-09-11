#!/usr/bin/env python
# -*- coding: utf-8 -*-

f=open('/etc/passwd','r')
# print(f)

for line in f:
	l=line.split(':')
	if l[3]>l[2]:
		print(" "+l[0]+"\t(uid: "+l[2]+",\tguid: "+l[3]+")")


