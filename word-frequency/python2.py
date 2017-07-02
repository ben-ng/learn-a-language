#!/usr/bin/python

from argparse import ArgumentParser
import re

p = ArgumentParser()
p.add_argument('n', type=int)
args = p.parse_args()
d = {}

with open('2cities.txt') as f:
	for line in f:
		for word in re.compile("[a-z]+", re.IGNORECASE).findall(line):
			nword = word.lower()
			
			# dict.[word] causes a KeyError if the key does not exist
			# but dict.get(word) does not!
			# 
			# Python's ternary operator looks like this:
			# (foo) if (condition) else (bar)
			d[nword] = 1 if d.get(nword) == None else d[nword] + 1

top = sorted(d.items(), key=lambda (_, cnt): cnt, reverse=True)[:args.n]

for (word, count) in top:
	print "%d %s" % (count, word)
