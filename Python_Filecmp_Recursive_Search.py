# Python filecmp
# filecmp — File and Directory Comparisons.
# The filecmp module defines functions to compare files and directories, with various optional time/correctness trade-offs.
#
# Here is a simplified example of using the subdirs attribute to search recursively through two directories to show common different files:
# 

#
# Comparing two directories.
#

from filecmp import dircmp

    def print_diff_files(dcmp):

        for name in dcmp.diff_files:
            print("diff_file %s found in %s and %s" % (name, dcmp.left,
                  dcmp.right))

        for sub_dcmp in dcmp.subdirs.values():
            print_diff_files(sub_dcmp)

dcmp = dircmp('dir1', 'dir2') 

print_diff_files(dcmp) 
