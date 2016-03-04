#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import sys
file = sys.argv[1]
bibFile = sys.argv[2]

with open(file,'rb') as csvfile:
	texto = '% Encoding: UTF-8\n\n'
	spamreader = csv.reader(csvfile,delimiter=',')		
	i = 1;
	for row in spamreader:				
		texto += '@article{Springer' + str(i) + ',\n' + '\t' + 'author = {' + row[6] + '},\n' +  '\t' + 'title = {' + row[0] + '},\n' + '\t' + 'journal = {' + row[1] + '},\n' +'\t' + 'year = {' + row[7] + '},\n' +	'}\n\n'
		i += 1
with open(bibFile,'a') as arq:
	arq.write(texto)	