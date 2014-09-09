#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unicodedata
from unicodedata import normalize, category

input_name=raw_input('Give your full name: ')
# separated_name=input_name.lower().split().reverse().join().decode('utf8')

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
