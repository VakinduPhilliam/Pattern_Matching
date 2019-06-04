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
# A command-line interface to difflib.
#

# 
# This example shows how to use difflib to create a diff-like utility.
# 

# !/usr/bin/env python3

""" Command line interface to difflib.py providing diffs in four formats:

* ndiff:    lists every line and highlights interline changes.
* context:  highlights clusters of changes in a before/after format.
* unified:  highlights clusters of changes in an inline format.
* html:     generates side by side comparison with change highlights.

"""

import sys, os, difflib, argparse
from datetime import datetime, timezone

def file_mtime(path):
    t = datetime.fromtimestamp(os.stat(path).st_mtime,
                               timezone.utc)

    return t.astimezone().isoformat()

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('-c', action='store_true', default=False,
                        help='Produce a context format diff (default)')

    parser.add_argument('-u', action='store_true', default=False,
                        help='Produce a unified format diff')

    parser.add_argument('-m', action='store_true', default=False,
                        help='Produce HTML side by side diff '
                             '(can use -c and -l in conjunction)')

    parser.add_argument('-n', action='store_true', default=False,
                        help='Produce a ndiff format diff')

    parser.add_argument('-l', '--lines', type=int, default=3,
                        help='Set number of context lines (default 3)')

    parser.add_argument('fromfile')

    parser.add_argument('tofile')

    options = parser.parse_args()

    n = options.lines
    fromfile = options.fromfile

    tofile = options.tofile

    fromdate = file_mtime(fromfile)
    todate = file_mtime(tofile)

    with open(fromfile) as ff:
        fromlines = ff.readlines()

    with open(tofile) as tf:
        tolines = tf.readlines()

    if options.u:
        diff = difflib.unified_diff(fromlines, tolines, fromfile, tofile, fromdate, todate, n=n)

    elif options.n:
        diff = difflib.ndiff(fromlines, tolines)

    elif options.m:
        diff = difflib.HtmlDiff().make_file(fromlines,tolines,fromfile,tofile,context=options.c,numlines=n)

    else:
        diff = difflib.context_diff(fromlines, tolines, fromfile, tofile, fromdate, todate, n=n)

    sys.stdout.writelines(diff)

if __name__ == '__main__':
    main()
