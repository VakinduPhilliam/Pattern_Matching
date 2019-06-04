# Python Difflib Pattern Matching
# difflib — Helpers for computing deltas
# This module provides classes and functions for comparing sequences.
# It can be used for example, for comparing files, and can produce difference information in various formats, including HTML and context and unified diffs.
#
# class difflib.SequenceMatcher 
# This is a flexible class for comparing pairs of sequences of any type, so long as the sequence elements are hashable.
# The basic algorithm predates, and is a little fancier than, an algorithm published in the late 1980’s by Ratcliff and Obershelp under the hyperbolic name
# “gestalt pattern matching.” 
# The idea is to find the longest contiguous matching subsequence that contains no “junk” elements; these “junk” elements are ones that are uninteresting in
# some sense, such as blank lines or whitespace.
# (Handling junk is an extension to the Ratcliff and Obershelp algorithm.)
# The same idea is then applied recursively to the pieces of the sequences to the left and to the right of the matching subsequence.
# This does not yield minimal edit sequences, but does tend to yield matches that “look right” to people.
# Timing: The basic Ratcliff-Obershelp algorithm is cubic time in the worst case and quadratic time in the expected case.
# SequenceMatcher is quadratic time for the worst case and has expected-case behavior dependent in a complicated way on how many elements the sequences have
# in common; best case time is linear.
# Automatic junk heuristic: SequenceMatcher supports a heuristic that automatically treats certain sequence items as junk.
# The heuristic counts how many times each individual item appears in the sequence.
# If an item’s duplicates (after the first one) account for more than 1% of the sequence and the sequence is at least 200 items long, this item is marked
# as “popular” and is treated as junk for the purpose of sequence matching.
# This heuristic can be turned off by setting the autojunk argument to False when creating the SequenceMatcher.
#
# class difflib.Differ 
# This is a class for comparing sequences of lines of text, and producing human-readable differences or deltas.
# Differ uses SequenceMatcher both to compare sequences of lines, and to compare sequences of characters within similar (near-matching) lines.
#

#
# Differ Example
# This example compares two texts.
#

#
# First we set up the texts, sequences of individual single-line strings ending with newlines (such sequences can also be obtained from the readlines()
# method of file-like objects):
# 

text1 = '''  1. Beautiful is better than ugly.
      2. Explicit is better than implicit.
      3. Simple is better than complex.
      4. Complex is better than complicated.
    '''.splitlines(keepends=True)

len(text1)

# OUTPUT: '4'

text1[0][-1]

# OUTPUT: '\n'

text2 = '''  1. Beautiful is better than ugly.
      3.   Simple is better than complex.
      4. Complicated is better than complex.
      5. Flat is better than nested.
    '''.splitlines(keepends=True)
 
#
# Next we instantiate a Differ object:
# 

d = Differ()


#
# Note that when instantiating a Differ object we may pass functions to filter out line and character “junk.”
#
 
#
# Finally, we compare the two:
# 

result = list(d.compare(text1, text2))

# 
# result is a list of strings, so let’s pretty-print it:
# 

from pprint import pprint

pprint(result)

#
# OUTPUT:
#
# ['    1. Beautiful is better than ugly.\n',
#  '-   2. Explicit is better than implicit.\n',
#  '-   3. Simple is better than complex.\n',
#  '+   3.   Simple is better than complex.\n',
#  '?     ++\n',
#  '-   4. Complex is better than complicated.\n',
#  '?            ^                     ---- ^\n',
#  '+   4. Complicated is better than complex.\n',
#  '?           ++++ ^                      ^\n',
#  '+   5. Flat is better than nested.\n']
#

# 
# As a single multi-line string it looks like this:
# 

import sys

sys.stdout.writelines(result)


#
# OUTPUT:
#
#    1. Beautiful is better than ugly.
# -   2. Explicit is better than implicit.
# -   3. Simple is better than complex.
# +   3.   Simple is better than complex.
# ?     ++
# -   4. Complex is better than complicated.
# ?            ^                     ---- ^
# +   4. Complicated is better than complex.
# ?           ++++ ^                      ^
# +   5. Flat is better than nested.
#