#!/usr/bin/env python3
import sys, collections, pprint

if len(sys.argv) < 2:
    filename = "wordlists/today"
else:
    filename = sys.argv[1]

infile = open(filename, "r")
words = infile.read().splitlines()
infile.close()

two_letter_list = {}
letter_count = {}

for word in words:
    tl = word[:2]
    if tl in two_letter_list:
        two_letter_list[tl] += 1
    else:
        two_letter_list[tl] = 1

    length = len(word)
    sl = word[:1]
    if sl not in letter_count:
        letter_count[sl] = {}

    if length in letter_count[sl]:
        letter_count[sl][length] += 1
    else:
        letter_count[sl][length] = 1

pprint.pprint(letter_count)
pprint.pprint(two_letter_list)
