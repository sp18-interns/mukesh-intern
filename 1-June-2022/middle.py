

def find_middle(x1,x2,x3):
    middle = (x1+x2+x3) - min(x1,x2,x3) - max(x1,x2,x3)
    return middle

def find_middle2(x1,x2,x3):
    middle = find_middle(x1,x2,x3)
    print ("Middle value is", middle)

val1 = input("First => ")
val2 = input("Second => ")
val3 = input("Third => ")

val1 = int(val1)
val2 = int(val2)
val3 = int(val3)

val = find_middle(val1, val2, val3)

print (val)
           
           
find_middle2(val1, val2, val3)           