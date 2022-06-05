

"""
Sort example

"""

scores = [59, 61, 63, 45, 68, 64, 58]

print (scores)

## correct way to call .sort() function
scores.sort()

print (scores)
print ("Min value is", scores[0])
print ("Max value is", scores[-1])

midpoint = len(scores)//2
print ("Middle value is", scores[midpoint])

##Incorrect way to call sort
##scores = scores.sort()
##print(scores)
## What went wrong?
## Don't do this, because .sort() returns nothing
## Don't assign it to a value

x = [1,4,5]
print ("Value of x when I start:", x)

val = input('Enter a value to add => ')

val = int(val)

print("Add this value to the list")
x.append(val)
print (x)

val = input('Enter a value to remove => ')
val = int(val)

if x.count(val) >= 1:
    x.remove(val)
else:
    print ("Value not in the list to remove")
print (x)

val = input("Enter a value to insert => ")
val = int(val)

idx = input("Which index to insert? => ")
idx = int(idx)

x.insert(idx, val)
print ("Value of x after:", x)

idx = input("Enter an index to pop => ")
idx = int(idx)

if idx < len(x) and idx > 0:
    val = x.pop(idx)
    print ("Popped value is", val)
    print ("Value of x after pop is", x)
else:
    print ("This is not a valid index to pop")
    print ("Popping the last value")
    val = x.pop()
    print ("Popped value is", val)
    print ("Value of x after pop is", x)

    #pop () is an inbuilt function in Python that removes and returns last value from the list or the given index value. index ( optional) - The value at index is popped out and removed. If the index is not given, then the last element is popped out and removed.
