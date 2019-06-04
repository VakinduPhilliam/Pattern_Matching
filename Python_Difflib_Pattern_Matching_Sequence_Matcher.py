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
# SequenceMatcher Objects:
#
# The SequenceMatcher class has this constructor:

#
# class difflib.SequenceMatcher(isjunk=None, a='', b='', autojunk=True): 
# Optional argument isjunk must be None (the default) or a one-argument function that takes a sequence element and returns true if and only if the element
# is “junk” and should be ignored. Passing None for isjunk is equivalent to passing lambda x: 0; in other words, no elements are ignored.
#
# For example, pass:
#

lambda x: x in " \t"
 
#
# if you’re comparing lines as sequences of characters, and don’t want to synch up on blanks or hard tabs.
#

# 
# The optional arguments a and b are sequences to be compared; both default to empty strings. The elements of both sequences must be hashable.
# 
# The optional argument autojunk can be used to disable the automatic junk heuristic.
#

#
# find_longest_match(alo, ahi, blo, bhi): 
# Find longest matching block in a[alo:ahi] and b[blo:bhi].
# 
# If isjunk was omitted or None, find_longest_match() returns (i, j, k) such that a[i:i+k] is equal to b[j:j+k], where alo <= i <= i+k <= ahi and blo <= j
# <= j+k <= bhi. For all (i', j', k') meeting those conditions, the additional conditions k >= k', i <= i', and if i == i', j <= j' are also met.
# In other words, of all maximal matching blocks, return one that starts earliest in a, and of all those maximal matching blocks that start earliest in a, 
# return the one that starts earliest in b.
# 

s = SequenceMatcher(None, " abcd", "abcd abcd")

s.find_longest_match(0, 5, 0, 9)

# OUTPUT: 'Match(a=0, b=4, size=5)'

#
# Here’s the same example as before, but considering blanks to be junk.
# That prevents ' abcd' from matching the ' abcd' at the tail end of the second sequence directly.
# Instead only the 'abcd' can match, and matches the leftmost 'abcd' in the second sequence:
# 

s = SequenceMatcher(lambda x: x==" ", " abcd", "abcd abcd")

s.find_longest_match(0, 5, 0, 9)

# OUTPUT: 'Match(a=1, b=0, size=4)'

#
# get_matching_blocks() 
# Return list of triples describing non-overlapping matching subsequences.
# Each triple is of the form (i, j, n), and means that a[i:i+n] == b[j:j+n].
# The triples are monotonically increasing in i and j.
#

# 
# The last triple is a dummy, and has the value (len(a), len(b), 0).
# It is the only triple with n == 0. If (i, j, n) and (i', j', n') are adjacent triples in the list, and the second is not the last triple in the list, then
# i+n < i' or j+n < j'; in other words, adjacent triples always describe non-adjacent equal blocks.
# 

s = SequenceMatcher(None, "abxcd", "abcd")

s.get_matching_blocks()

# OUTPUT: '[Match(a=0, b=0, size=2), Match(a=3, b=2, size=2), Match(a=5, b=4, size=0)]'
 
#
# get_opcodes() 
# Return list of 5-tuples describing how to turn a into b.
# Each tuple is of the form (tag, i1, i2, j1, j2).
# The first tuple has i1 == j1 == 0, and remaining tuples have i1 equal to the i2 from the preceding tuple, and, likewise, j1 equal to the previous j2.
#

#
# For example:
# 

a = "qabxcd"
b = "abycdf"

s = SequenceMatcher(None, a, b)

for tag, i1, i2, j1, j2 in s.get_opcodes():
        print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(
            tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))

#
# real_quick_ratio(): 
# Return an upper bound on ratio() very quickly.
# The three methods that return the ratio of matching to total characters can give different results due to differing levels of approximation, although
# quick_ratio() and real_quick_ratio() are always at least as large as ratio():
# 

s = SequenceMatcher(None, "abcd", "bcde")

s.ratio()

# OUTPUT: '0.75'

s.quick_ratio()

# OUTPUT: '0.75'

s.real_quick_ratio()

# OUTPUT: '1.0'
