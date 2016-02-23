#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import sys
file = sys.argv[1]
bibFile = sys.argv[2]

with open(file,'rb') as csvfile:
	texto = '% Encoding: UTF-8\n\n'
	spamreader = csv.reader(csvfile,delimiter='\t')		
	i = 1;
	for row in spamreader:				
		texto += '@Article{WEBOFSCI' + str(i) + ',\n' + '\t' + 'author={' + row[1] + '},\n' +  '\t' + 'title={' + row[9] + '},\n' + '\t' + 'journal={' + row[17] + '},\n' +'\t' + 'year={' + row[32] + '},\n' +		'\t' + 'abstract={' + row[33] + '}\n' +		'}\n\n'
		i += 1
	with open(bibFile,'a') as arq:
		arq.write(texto)	