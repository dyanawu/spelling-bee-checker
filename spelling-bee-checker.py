#!/usr/bin/env python3
import sys, collections

if len(sys.argv) < 2:
    filename = "wordlists/today"
else:
    filename = sys.argv[1]

infile = open(filename, "r")
words = infile.read().splitlines()
infile.close()

word_lengths = []
letter_count = {}
two_letter_list = {}
word_count = 0

for word in words:
    word_count += 1
    length = len(word)
    sl = word[:1]
    if sl not in letter_count:
        letter_count[sl] = {}

    if length in letter_count[sl]:
        letter_count[sl][length] += 1
    else:
        letter_count[sl][length] = 1

    tl = word[:2]
    if sl not in two_letter_list:
        two_letter_list[sl] = {}

    if tl in two_letter_list[sl]:
        two_letter_list[sl][tl] += 1
    else:
        two_letter_list[sl][tl] = 1

    if length not in word_lengths:
        word_lengths.append(length)
    else:
        continue

word_lengths.sort()
letter_count_grid = {}

for sl in letter_count:
    for i in range (word_lengths[0], word_lengths[-1]+1):
        letter_count_grid[sl] = [str(letter_count[sl][i]) if i in letter_count[sl] else "-" for i in word_lengths]

print(f"\nWords found: {word_count}")

print("\nWord lengths:\n")
print(f"    {'  '.join([str(i) for i in word_lengths])}")
for row in letter_count_grid:
    print(f"{row}:  " + "  ".join(letter_count_grid[row]))

print("\nTwo letter list:\n")
for tl in two_letter_list:
    tl_list = [f"{key.upper()}-{value}" for key, value in two_letter_list[tl].items()]
    print(" ".join(tl_list))
