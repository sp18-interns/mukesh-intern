 Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple
n = int(input())
data = namedtuple("data",input())
marks_lst = []
for i in range(n):
    marks = int(data(*input().split()).MARKS)
    marks_lst.append(marks)
print(sum(marks_lst)/n)