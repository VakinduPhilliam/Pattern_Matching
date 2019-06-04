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
# consider a directory containing the following files: 1.gif, 2.txt, card.gif and a subdirectory sub which contains only the file 3.txt. glob() will produce
# the following results.
#
# Notice how any leading components of the path are preserved.
# 

import glob

glob.glob('./[0-9].*')

# OUTPUT: '['./1.gif', './2.txt']'

glob.glob('*.gif')

# OUTPUT: '['1.gif', 'card.gif']'

glob.glob('?.gif')

# OUTPUT: '['1.gif']'

glob.glob('**/*.txt', recursive=True)

# OUTPUT: '['2.txt', 'sub/3.txt']'

glob.glob('./**/', recursive=True)

# OUTPUT: '['./', './sub/']'
