# mukesh-intern

# 06 April 2022

## First Half

- Topic

  - ✅ Hackerrank questions
  - (Text Wrap)
  - (String Formatting)
  - (Capitalize)
  - (itertoola.product())



## Videos

- N/A

### Assignment

- ✅  Hackerrank questions solved

### Doubts

-  No doubts

### Links


- https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
- https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
- https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
- https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true

## Second Half

### Topic
-  collections.Counter()
- Polar Coordinates
- Questions of codingbat 


### Videos

- N/A

### Assignment 

- Hackerrank question solved

### Doubts

- No doubts 

### Links
- https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
- https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

 Q.1
 collections.Counter()
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

Sample Code

>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]
Task

 is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.

Input Format

The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.

Constraints





Output Format

Print the amount of money earned by .

Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output

200
Explanation

Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.

Total money earned = 

## code
TDOUT
n=int(input())

stock = list(map(int,input().split(' ')))

# stocks to be printed
from collections import Counter

Dict=Counter(stock)

x=int(input())

p=0
for i in range(x):
    size,price= map(int,input().split(' '))
    
    if Dict[size]:
        Dict[size]-=1
        p=p+price
print(p)

 Q.2
Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.

A complex number  Capture.PNG

is completely determined by its real part  and imaginary part .
Here,  is the imaginary unit.
A polar coordinate () Capture.PNG

is completely determined by modulus  and phase angle .

If we convert complex number  to its polar coordinate, we find:
: Distance from  to origin, i.e., 
: Counter clockwise angle measured from the positive -axis to the line segment that joins  to the origin.

Python's cmath module provides access to the mathematical functions for complex numbers.


This tool returns the phase of complex number  (also known as the argument of ).

>>> phase(complex(-1.0, 0.0))
3.1415926535897931

This tool returns the modulus (absolute value) of complex number .

>>> abs(complex(-1.0, 0.0))
1.0
Task
You are given a complex . Your task is to convert it to polar coordinates.

Input Format

A single line containing the complex number . Note: complex() function can be used in python to convert the input as a complex number.

Constraints

Given number is a valid complex number

Output Format

Output two lines:
The first line should contain the value of .
The second line should contain the value of .

Sample Input

  1+2j
Sample Output

 2.23606797749979 
 1.1071487177940904
Note: The output should be correct up to 3 decimal places.

## code
# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
c = complex(input().strip())

res=cmath.polar(c)
print(res[0])
print(res[1])

Q.3
itertools.permutations(iterable[, r])

This tool returns successive  length permutations of elements in an iterable.

If  is not specified or is None, then  defaults to the length of the iterable, and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.

Sample Code

>>> from itertools import permutations
>>> print permutations(['1','2','3'])
<itertools.permutations object at 0x02A45210>
>>> 
>>> print list(permutations(['1','2','3']))
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
>>> 
>>> print list(permutations(['1','2','3'],2))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
>>>
>>> print list(permutations('abc',3))
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
Task

You are given a string .
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.

Input Format

A single line containing the space separated string  and the integer value .

Constraints


The string contains only UPPERCASE characters.

Output Format

Print the permutations of the string  on separate lines.

Sample Input

HACK 2
Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
Explanation

All possible size  permutations of the string "HACK" are printed in lexicographic sorted ord

## code
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s,n=input().split(' ')

for i in list(permutations(sorted(s),int(n))):
    print(''.join(i))

Q.4
Check Tutorial tab to know how to to solve.

You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns

string: a single string with newline characters ('\n') where the breaks should be
Input Format

The first line contains a string, .
The second line contains the width, .

Constraints

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

## code


def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':

Q.5


You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

chris alan
Sample Output

Chris Alan

## code


import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(s):
    l = s.split(" ")
    s=''
    for i in l:
        s=s+i.capitalize()+' '
        
    return s

if __name__ == '__main__':


