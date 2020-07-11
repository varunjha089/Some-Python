"""
    7.2. Reading and Writing Files
"""

# The first argument is a string containing the filename. The second argument is another string containing a few
# characters describing the way in which the file will be used. mode can be 'r' when the file will only be read,
# 'w' for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending;
# any data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing.
# The mode argument is optional; 'r' will be assumed if it’s omitted.

f = open('workfile', 'w')

with open('workfile') as f:
    read_data = f.read()
f.closed
