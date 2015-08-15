#!/usr/bin/env python

""" Simple word generator that can be used for generating words of a 
    defined pattern and length. Define character sets as strings, set pattern
    to be a tuple made up of those sets to the desired string length,
    and it will generate all permutations of those sets for that
    length.
    
    Please see the LICENSE file attached to the source repository for license information.

    Matthew Scheffel <mscheffel@gmail.com>
"""

from string import ascii_lowercase
import re

def fill_position(position, length, partial):
    """ Recursive method that will iterate over the character
    set assigned for the current position in the string. If
    it is at the last position, it prints to STDOUT. """

    if position == length - 1:
        for character in pattern[position]:
            print "%s%s" % (partial, character)
    else:
        for character in pattern[position]:
            fill_position(position+1, length, partial+character)

ascii_consonants = re.sub("[aeiou]", "", ascii_lowercase)
ascii_vowels = "aeiou"

# left-handed consonants on a qwerty keyboard
#ascii_consonants = "qwrtsdfgzxcv"

# left-handed vowels on a qwerty keyboard
#ascii_vowels = "ae"

V = ascii_vowels
C = ascii_consonants

pattern = (C, V, V, C, V)
length  = len(pattern)

fill_position(0, length, "")
