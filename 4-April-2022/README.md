# mukesh-intern

# 04 April 2022

## First Half

- Topic

  - ✅ Snake Water Game



## Videos

- Analyze code of Game

### Assignment

- ✅  Snake Water Game -Completed

### Doubts

-  No doubts

### Links


- https://thepythonguru.com/python-string-formatting/
- https://www.geeksforgeeks.org/python-randint-function/

## Second Half

### Topic
-  Hackerrank Questions
- (-Finding the percentage)
- (-Lists)
- (-Tuples)
- (-sWAp cASE)
- (-What's Your Name?) 


### Videos

- N/A

### Assignment 

- Solved questions of  Hackerrank

### Doubts

- No doubts

### Links

- https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
- https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
- https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
- https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
- https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true

Q.1
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Example




The query_name is 'beta'. beta's average score is .

Input Format

The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

Constraints

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input 0

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output 0

56.00
Explanation 0

Marks for Malika are  whose average is 

Sample Input 1

2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
Sample Output 1

26.50

### Code-

    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

Q.2

Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example





: Append  to the list, .
: Append  to the list, .
: Insert  at index , .
: Print the array.
Output:
[1, 3, 2]
Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

### Code-

if __name__ == '__main__':
    N = int(input())

  Q.3

  Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer, , denoting the number of elements in the tuple.
The second line contains  space-separated integers describing the elements in tuple .

Output Format

Print the result of .

Sample Input 0

2
1 2
Sample Output 0

3713081631934410656

### Code-

    integer_list = map(int, input().split())

Q.4

You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
Function Description

Complete the swap_case function in the editor below.

swap_case has the following parameters:

string s: the string to modify
Returns

string: the modified string
Input Format

A single line containing a string .

Constraints


Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".

### Code-

def swap_case(s)
:
    return s.swapcase()
 Q.5

 You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.

Function Description

Complete the print_full_name function in the editor below.

print_full_name has the following parameters:

string first: the first name
string last: the last name
Prints

string: 'Hello  ! You just delved into python' where  and  are replaced with  and .
Input Format

The first line contains the first name, and the second line contains the last name.

Constraints

The length of the first and last names are each ≤ .

Sample Input 0

Ross
Taylor
Sample Output 0

Hello Ross Taylor! You just delved into python.
Explanation 0

The input read by the program is stored as a string data type. A string is a collection of character

### Code-


     print("Hello %s %s! You just delved into python."%(a,b))

if __name__=='__main__'..

