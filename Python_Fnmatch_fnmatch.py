# Python Fnmatch
# fnmatch — Unix filename pattern matching.
# This module provides support for Unix shell-style wildcards, which are not the same as regular expressions.
#
# The special characters used in shell-style wildcards are:
# * - matches everything
# ? - matches any single character
# [seq] - matches any character in seq
# [!seq] - matches any character not in seq
# 
# For a literal match, wrap the meta-characters in brackets.
#
# For example, '[?]' matches the character '?'.
# 
# Note that the filename separator ('/' on Unix) is not special to this module. 
# Similarly, filenames starting with a period are not special for this module, and are matched by the * and ? patterns.
#

#
# fnmatch.fnmatch(filename, pattern): 
# Test whether the filename string matches the pattern string, returning True or False. Both parameters are case-normalized using os.path.normcase().
# fnmatchcase() can be used to perform a case-sensitive comparison, regardless of whether that’s standard for the operating system.
# 

#
# This example will print all file names in the current directory with the extension .txt:
# 

import fnmatch
import os

for file in os.listdir('.'):

    if fnmatch.fnmatch(file, '*.txt'):

         print(file)
