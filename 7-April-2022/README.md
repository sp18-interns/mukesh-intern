# mukesh-intern

# 07 April 2022

## First Half

- Topic

  - ✅ Hackerrank questions
  - (Intoductions of sets)
  - (Mutations)
  - (codingbat)



## Videos

- N/A

### Assignment

- ✅  Hackerrank questions solved

### Doubts

-  No doubts

### Links


- https://codingbat.com/prob/p120546


## Second Half

### Topic
-   Designer Doormat


### Videos

- N/A

### Assignment 

- Hackerrank question solved

### Doubts

- No doubts 

### Links
-https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true

Q.1
A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

Example

>>> print set()
set([])

>>> print set('HackerRank')
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

>>> print set([1,2,1,2,3,4,5,6,0,9,12,22,3])
set([0, 1, 2, 3, 4, 5, 6, 9, 12, 22])

>>> print set((1,2,3,4,5,5))
set([1, 2, 3, 4, 5])

>>> print set(set(['H','a','c','k','e','r','r','a','n','k']))
set(['a', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print set({'Hacker' : 'DOSHI', 'Rank' : 616 })
set(['Hacker', 'Rank'])

>>> print set(enumerate(['H','a','c','k','e','r','r','a','n','k']))
set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])
Basically, sets are used for membership testing and eliminating duplicate entries.

Task

Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used:

Function Description

Complete the average function in the editor below.

average has the following parameters:

int arr: an array of integers
Returns

float: the resulting float value rounded to 3 places after the decimal
Input Format

The first line contains the integer, , the size of .
The second line contains the  space-separated integers, .

Constraints


Sample Input

STDIN                                       Function
-----                                       --------
10                                          arr[] size N = 10
161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]
Sample Output

169.375
Explanation

Here, set is the set containing the distinct heights. Using the sum() and len() functions, we can compute the average.

## code
def average(array):
    
    array = set(array)
    return sum(array)/len(array)
    # your code goes here

if __name__ == '__main__':

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

abrackdabra

## code
def mutate_string(string, position, character):
    return string[:position]+character+string[position+1:]

Q.3

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
Input Format

A single line containing the space separated values of  and .

Constraints

Output Format

Output the design pattern.

Sample Input

9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.-

## code
# Enter your code here. Read input from STDIN. Print output to STDOUT
R,C = map(int,input().split(' '))

for i in range(1,R,2):
    print((".|."*i).center(C,'-'))
    
print("WELCOME".center(C,'-'))

for i in range(R-2,-1,-2):
    print((".|."*i).center(C,'-'))
 

Q.4
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.


monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False

## code
ef monkey_trouble(a_smile, b_smile):
  if a_smile ==True and b_smile == True:
    return True
  elif a_smile ==False and b_smile == False:
    return True  
  elif a_smile ==True and b_smile == False:
    return False
  elif a_smile ==False and b_smile == True:
    return False   