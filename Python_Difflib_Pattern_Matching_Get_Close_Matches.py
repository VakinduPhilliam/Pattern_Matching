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
# difflib.get_close_matches(word, possibilities, n=3, cutoff=0.6): 
# Return a list of the best “good enough” matches. word is a sequence for which close matches are desired (typically a string), and possibilities is a list
# of sequences against which to match word (typically a list of strings).
#
 
#
# Optional argument n (default 3) is the maximum number of close matches to return; n must be greater than 0.
# Optional argument cutoff (default 0.6) is a float in the range [0, 1]. Possibilities that don’t score at least that similar to word are ignored.
#

# 
# The best (no more than n) matches among the possibilities are returned in a list, sorted by similarity score, most similar first.
# 

get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'])

# OUTPUT: '['apple', 'ape']'

import keyword

get_close_matches('wheel', keyword.kwlist)

# OUTPUT: '['while']'

get_close_matches('pineapple', keyword.kwlist)

# OUTPUT: '[]'

get_close_matches('accept', keyword.kwlist)

# OUTPUT: '['except']'
