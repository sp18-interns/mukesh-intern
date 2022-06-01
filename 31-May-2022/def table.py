# Python Program to print table of number
# using a function

# define function

def table(n):
    for i in range(1,11):

       print(n,"x",i,"=",n*1)

#main
# input number

n = int(input("Enter nnumber:"))

# call table function
#  
table(n)