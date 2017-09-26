#!/usr/bin/env python
import csv
with open('names.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter= ' ', quotechar='|')
	for row in spamreader:
		print ', '.join(row)