

## Add up values greater than 3

x = [1,3,5,8,2,1,7]

i = 0
valsum = 0

while i < len(x):
    if x[i] > 3:
        valsum += x[i]
    i += 1
    
print ("Sum of values greater than 3:", valsum)
print ("Sum of values(built-in):", sum(x))

###Compare values side by side, absolute difference
##of values side by side
i = 0
diffsum = 0
while i < len(x)-1:
    print("i",i, "Values:", x[i], x[i+1] )
    diffsum += abs(x[i]-x[i+1])
    i += 1
    
print ("Total Difference:", diffsum)

## count number of consecutive letters that are the same
## in a word

x = "bookkeeper"

i = 0
cnt = 0 ##number of consecutive double letters
while i < len(x)-1:
    if x[i] == x[i+1]:
        cnt += 1
    i += 1
print ("Number of consecutive double letters in",x,"is",cnt)

##generate all pairs of values from a list

animals = ['dog','cat','bird','vulture','platypus','giraffe']


i = 0
while i < len(animals):
    j=0
    while j < len(animals):
        print (animals[i], animals[j])
        j += 1
    
    i += 1
    

## read values until user enters STOP

not_finished = True
while not_finished:
    ans = input("Enter something, STOP to stop ==> ")
    
    if ans.upper() == 'STOP':
        not_finished = False
    