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
# SequenceMatcher Examples
#

# 
# This example compares two strings, considering blanks to be “junk”:
# 

s = SequenceMatcher(lambda x: x == " ",
                        "private Thread currentThread;",
                        "private volatile Thread currentThread;")
 
#
# ratio() returns a float in [0, 1], measuring the similarity of the sequences.
# As a rule of thumb, a ratio() value over 0.6 means the sequences are close matches:
# 

print(round(s.ratio(), 3))

# OUTPUT: '0.866'
 
#
# If you’re only interested in where the sequences match, get_matching_blocks() is handy:
# 

for block in s.get_matching_blocks():

           print("a[%d] and b[%d] match for %d elements" % block)

#
# Note that the last tuple returned by get_matching_blocks() is always a dummy, (len(a), len(b), 0), and this is the only case in which the last tuple
# element (number of elements matched) is 0.
#

# 
# If you want to know how to change the first sequence into the second, use get_opcodes():
# 

for opcode in s.get_opcodes():

           print("%6s a[%d:%d] b[%d:%d]" % opcode)
