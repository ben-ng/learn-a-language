#!/usr/bin/python

from argparse import ArgumentParser
from collections import defaultdict
import itertools
import re

p = ArgumentParser()
p.add_argument('n', type=int)
args = p.parse_args()

# use int as the default_factory
# int() is called to supply a default value of 0
d = defaultdict(int)

# this implicitly closes the file when done
with open('2cities.txt') as f:
	# this creates a lazy iterator
	words = itertools.imap(lambda line: re.compile("[a-z]+", re.IGNORECASE).findall(line), f)
	
	# the chain.from_iterable flattens words (there's no flatmap)
	for word in itertools.chain.from_iterable(words):
		d[word.lower()] += 1

# (_, cnt) destructures the tuples we get from d.items(), [:n] slices results
for (word, count) in sorted(d.items(), key=lambda (_, cnt): cnt, reverse=True)[:args.n]:
	print "%d %s" % (count, word)
