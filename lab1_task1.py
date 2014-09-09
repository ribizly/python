#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_type=raw_input('Input type: ')
input_temp=input('Input temperature: ')

if (input_type=='C'):
    F=(input_temp*9/5+32)
    print('Output: %d F' % F )
elif (input_type=='F'):
    C=5*(input_temp-32)/ 9
    print('Output: %d C' % C )
else: print('Invalid type')
