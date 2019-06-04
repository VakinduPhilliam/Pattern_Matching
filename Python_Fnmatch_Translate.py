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
# fnmatch.translate(pattern). 
# Return the shell-style pattern converted to a regular expression for using with re.match().
# 

#
# Example:
# 

import fnmatch, re

regex = fnmatch.translate('*.txt')
regex

# OUTPUT: '(?s:.*\\.txt)\\Z'

reobj = re.compile(regex)
reobj.match('foobar.txt')

# OUTPUT: '<re.Match object; span=(0, 10), match='foobar.txt'>'


