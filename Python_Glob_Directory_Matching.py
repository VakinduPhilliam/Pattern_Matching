# Python Glob
# glob — Unix style pathname pattern expansion.
# The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in
# arbitrary order.
# No tilde expansion is done, but *, ?, and character ranges expressed with [] will be correctly matched.
# This is done by using the os.scandir() and fnmatch.fnmatch() functions in concert, and not by actually invoking a subshell.
#
# Note that unlike fnmatch.fnmatch(), glob treats filenames beginning with a dot (.) as special cases.
# (For tilde and shell variable expansion, use os.path.expanduser() and os.path.expandvars().)
# 
# For a literal match, wrap the meta-characters in brackets.
#
# For example, '[?]' matches the character '?'.
#

#
# If the directory contains files starting with . they won’t be matched by default.
#
# For example, consider a directory containing card.gif and .card.gif:
# 

import glob

glob.glob('*.gif')

# OUTPUT: '['card.gif']'

glob.glob('.c*')

# OUTPUT: '['.card.gif']'
