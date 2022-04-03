# mukesh-intern

# 31 March 2022

## First Half

- Topic

  - Questions of hackerrank
  - Practice sets



## Videos

- Codewithharry
- Python tutorials

### Assignment

- Hackerrank questions solved
-  Assignment of harry

### Doubts

-  Cleared by Avinash sir 

### Links


- https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
- https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

## Second Half

### Topic
-  Analyze the code

### Videos

- N/A

### Assignment 

- Hackerrank  Questions

### Doubts

- Doubts cleared by our Team

### Links

- https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/



 # Questions of hackerrank

 ## Q.1
Task
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up scor

  ## Code
 if __name__ == '__main__':
    n = int(input())
    arr =list(map(int, input().split()))
    arr.sort()
    print(arr[(arr.index(max(arr)))-1])
    

## Q.2

Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta
Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
Explanation 0

There are  students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line

 ## Code

 if __name__ == '__main__':
    dic = {}
    s = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in dic:
            dic[score].append(name)
        else:
            dic[score] = [name]
        if score not in s:
            s.append(score)
            
m = min(s)
s.remove(m)
m1 = min(s)
dic[m1].sort()
for i in dic[m1]:
    print(i)

## Q.3

Let's learn about list comprehensions! You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n . Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. Here, 0 =< i =< x; 0 =< j =< y; 0 =< k =< z. Please u k <e list comprehensions rather than multiple loops, as a learning exercise.

Example
x=1
y=1
z=2
n=3




All permutations of[i,j,k]  are:
.

Print an array of the elements that do not sum to n = 3 .


Input Format

Four integers x,y,z  and n , each on a separate line.

Constraints

Print the list in lexicographic increasing order.

Sample Input 0

1
1
1
2
Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
Explanation 0

Each variable x,y and z  will have values 0 or 1 of  or . All permutations of lists in the form .
Remove all arrays that sum to  n = 2 to leave only the valid permutations.

Sample Input 1

2
2
2
2
Sample Output 1

[[0, 0, 0], [0, 0,1][https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true]