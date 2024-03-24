"""
Homework 10. Regexp.

open input.txt file and find all small english letters
that match such conditions:

target small letter round exactly with three capital english letters
on the left and on the right
Match examples:
sdTRYaUVKn  -> matches "a" because 'TRY' on the left
( 3 capital letters ) and 'UVK' on the right ( 3 capital letters)
NTRSjARTb   -> no match ( not exactly 3 capital letters
on the left ('NTRS' = 4 letters) )
zDFGbOPNq   -> matches "b"
Print Output as : "Result: "string of found letters".
"""

import re

with open('input.txt') as in_file:
    in_str = in_file.read()

out = re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', in_str, re.MULTILINE)
print('Result: "' + ''.join(out) + '"')
