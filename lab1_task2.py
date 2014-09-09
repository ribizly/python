#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

while 1:

    try:
        input_type=raw_input('Input type: ')
    except Exception as e:
        print 'Elszallunk'
        sys.exit(0)

    input_temp=input('Input temperature: ')

    if (input_type.lower()=='c'):
        F=(input_temp*9/5+32)
        print('Output: %d F' % F )

    elif (input_type.lower()=='f'):
        C=5*(input_temp-32)/ 9
        print('Output: %d C' % C )

    else: print('Invalid type %s' % input_type)
    print('\n')
