num = int(input("enter the number"))

n = num

reverse = 0

while n != 0:

    rem = n % 10

    reverse = reverse * 10 + rem

    n = n//10

print("{} is reverse of {}".format(reverse,num))


n=8
a=[]
while(n>0):
    if 0<1:
        print('1')
    var=n%2
    a.append(var)
    n=n//2
a.reverse()

for i in a:
    print(i,end=" ") 


set1 = {1,2,3,int('4')}
set2 = {3,str(4)}
print(set1.union(set2))