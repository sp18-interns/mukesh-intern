a = [ 1,1,2,3,4,5,6,7,8,9,10,15,18]

for x in a:
    if x < 10:
        print(x)

print([x for x in a if x<5])