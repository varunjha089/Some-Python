"""
    @author
    Varun Kumar

    7.1. Fancier Output Formatting
"""

import math

# To use formatted string literals, begin a string with f or F before the opening quotation mark or triple quotation
# mark. Inside this string, you can write a Python expression between { and } characters that can refer to variables or
# literal values.

year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

name = 'varun kumar'
dob = '19-11-1997'

print(f'{name.upper()} born in the year {dob}')

# The str.format() method of strings requires more manual effort. You’ll still use { and } to mark where a variable
# will be substituted and can provide detailed formatting directives, but you’ll also need to provide the information
# to be formatted.

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

print('{} born in year {}'.format(name.upper(), dob))

"""
    When you don’t need fancy output but just want a quick display of some variables for debugging purposes, you can
    convert any value to a string with the repr() or str() functions.

    The str() function is meant to return representations of values which are fairly human-readable, while
    repr() is meant to generate representations which can be read by the interpreter
    (or will force a SyntaxError if there is no equivalent syntax).
"""

s = 'Hello, world.'
print(str(s))  # str() will give the string as output Hello, world.

print(repr(s)) # repr() will give the value of s 'Hello, world.'

print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

t = f'The value of x is {repr(x)}, and y is {repr(y)}...'
print(t)

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))))


"""
    7.1.1. Formatted String Literals

    Formatted string literals (also called f-strings for short) let you include the value of Python expressions
    inside a string by prefixing the string with f or F and writing expressions as {expression}.
"""

print(f'The value of pi is approximately {math.pi:.48f}.')

"""
    Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful
    for making columns line up.
"""
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')


"""
    Other modifiers can be used to convert the value before it is formatted. '!a' applies ascii(),
    '!s' applies str(), and '!r' applies repr():
"""

animals = 'eels'
print(f'My hovercraft is full of {animals}.')

print(f'My hovercraft is full of {animals!r}.')

"""
    7.1.2. The String format() Method
"""

# Basic usage of the str.format() method looks like this:

print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('{0} and {1}'.format('spam', 'eggs'))

print('{1} and {0}'.format('spam', 'eggs'))

for x in range(1, 11):
    print('{0:4d} {1:4d} {2:4d}'.format(2*x, 3*x, 4*x))

"""
    7.1.3. Manual String Formatting
"""

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))