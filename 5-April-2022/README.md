# mukesh-intern

# 05 April 2022

## First Half

- Topic

  - ✅ Hackerrank questions
  - (String Split and Join)
  - (Mutations)
  - (Find a string)
  - (String Validators)



## Videos

- N/A

### Assignment

- ✅  Hackerrank questions solved

### Doubts

-  No doubts

### Links


- https://www.geeksforgeeks.org/python-check-substring-present-given-string/

## Second Half

### Topic
-  Health Management system


### Videos

- Codewithharry on youtube

### Assignment 

- 🔄 Health management   System

### Doubts

- No doubts till now

### Links
- https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
- https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
- https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
- https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true

 Q.1

 In Python, a string can be split on a delimiter.

Example:

>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']
Joining a string is simple:

>>> a = "-".join(a)
>>> print a
this-is-a-string 
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Function Description

Complete the split_and_join function in the editor below.

split_and_join has the following parameters:

string line: a string of space-separated words
Returns

string: the resulting string
Input Format
The one line contains a string consisting of space separated words.

Sample Input

this is a string   
Sample Output

this-is-a-string

 ## Code


def split_and_join(line):
    return '-'.join(line.split(" "))
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

Q.2
We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Let's try to understand this with an example.

You are given an immutable string, and you want to make changes to it.

Example

>>> string = "abracadabra"
You can access an index by:

>>> print string[5]
a
What if you would like to assign a value?

>>> string[5] = 'k' 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
How would you approach this?

One solution is to convert the string to a list and then change the value.
Example

>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra
Another approach is to slice the string and join it back.
Example

>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra
Task
Read a given string, change the character at a given index and then print the modified string.
Function Description

Complete the mutate_string function in the editor below.

mutate_string has the following parameters:

string string: the string to change
int position: the index to insert the character at
string character: the character to insert
Returns

string: the altered string
Input Format

The first line contains a string, .
The next line contains an integer , the index location and a string , separated by a space.

Sample Input

STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'
Sample Output

## code
position, character):
    return string[:position]+character+string[position+1:]

if __name__ == '__main__':

Q.3
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2
Concept

Some string processing examples, such as these, might be useful.
There are a couple of new concepts:
In Python, the length of a string is found by the function len(s), where  is the string.
To traverse through the length of a string, use a for loop:

for i in range(0, len(s)):
    print (s[i])
A range function is used to loop over some length:

range (0, 5)
Here, the range loops over  to .  is excluded.

## code
sub_string):
    
    ml=len(string)
    sl=len(sub_string)
    c = 0
    
    for i in range(ml-sl+1):
        if(string[i:(i+sl)]== sub_string):
            c=c+1
    return c

if __name__ == '__main__':

Q.4
Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False
str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False
str.isdigit()
This method checks if all the characters of a string are digits (0-9).

>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False
str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).

>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False
str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).

>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False
Task

You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

Sample Input

qA2
Sample Output

True
True
True
True
True

 ## code
 
    s = input()
    print(any([i.isalnum() for i in s]))
    print(any([i.isalpha() for i in s]))
    print(any([i.isdigit() for i in s]))
    print(any([i.islower() for i in s]))
    print(any([i.isupper() for i in s]))