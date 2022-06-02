"""

New data type:

Boolean: True or False

Conditions can be built by

>
< 
>=  (not =>)
<=
==  (is same?)
!=  (is not same?)

Returns true or false

You can compare numbers

You can compare strings: lexicographic ordering
(dictionary ordering)

1. alphabetical first: check character by character
until you first character that is different 
2. shorter strings are smaller than longer strings (if the beginning of two strings is the same, shorter is smaller)
ex. 'aa' < 'aaa'
3. numbers first, then upper case and then lower case

The following are all true:
'a' < 'b' -- a is smaller than b
'a' < 'aa' -- shorter string is smaller
'aab' < 'ab'  -- 'aa' is less than 'ab' becase
              a's are the same and a is 
              smaller than b
Capital letter first

'A' < 'a'   --- capital letters are smaller

Numbers are based on Ascii code

'9' < 'a'   --- all numbers are smaller than 
                all letters

'9' < 'A'

Complex conditions:

True and True = True
True and False = False
False and True = False
False and False = False

True or True = True
True or False = True
False or True = True
False or False = False

not True = False
not False = True

Simple logic:

not (a and b) = (not a) or (not b) 
not (a or b) = (not a) and (not b) 

not (not a) = a

"""