"""
List aliasing vs. copying

L1 = [1,2,3]
L2 = L1

## L2 is an alias to L1, if I change L1 or L2
same list is changed

L3 = L1.copy()

L3 is identical L1, but it is a different copy
so changes to L3 will not effect L1 and vice versa

Remember: when you use a list as an argument
to a function: it is an alias
-> If you change the list in the function, then
the list is changed outside of the function.

Functions that modify a list (but does not return a new list):

.sort(), .append(), .pop(), .remove(), .insert()

Functions that return a new list

.copy(), slicing, concatenation, replication


while loops over numbers which we can use
to index items in a list

for loops to iterate over items in a list

"""

def f1(x):
    x[0] += 1
    
def f2(x):
    x[0] = x[0]*20
    x.sort()
    
a = [1,5]

print ("a before the function f1:", a)
f1(a)
print ("a after the function f1:", a)

print ("a before the function f2:", a)
f2(a)
print ("a after the function f2:", a)