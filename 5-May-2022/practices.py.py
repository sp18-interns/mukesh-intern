squares = []
remain = []

for i in range(1,11):
    if i % 2 == 0:
        squares.append(i**2)
    else:
        remain.append(i**2)






print(squares)
print(remain)

for i in range(1,4):
    print(i)
else:
    print("No Break")





for i in range(1,5):
    print(i)
    break
else:
    print("No Break")



a = 2
b = 4

if a<b:
    print(a, 'is less than ', b)
else:
    print(a,'is not less than',b)




a = 5
b = 8

if a >= b:
    print('Its good')
else:
    print('Its not good')





a = 2
b = 4
c = 5

if a < b:
    print(a,'is less than', b)
    if c < b:
        print(c,'is less than ',b)
    else:
        print(c,'Is not less than ',b)
else:
    print(a,'is not less than',b)



num =2

for i in range(1,11):
    print(num,'x',i,'=',num*i)



counter = 1
while (counter < 5):
    count = counter
    if count < 2:
        counter = counter + 1
    else:
        print('less than 2')
    if  count > 4:
        counter = counter+ 1
    else:
        print('Greater than 4')
    counter = counter + 1




i = 0
while i<5:
    if i==3:
        break
    print(i)
    i=i+1

else:
    print("inside else")




n = 11
for i in range(0,n):
    for j in range(0,n):
        if j == n//2 or i ==n//2 or (i>n//2 and j ==n-1) or ( i == n-1 and j <=n//2) or ( i<n//2 and j==0) or (i ==0 and j >n//2) or (( i == ((n//2 + (n//2)//2)+1) and ( j == ((n//2 + (n//2)//2))+1) ) or ((i ==((n//2) + (n//2)//2+1)) and j ==((((n//2)//2)//2 )+1) or (i == n%10+1 and j == n%10+1)) or (i==(n//2)//2 and j ==(n//2)+3) ): 
            print(" * ", end = '') 
        else:
            print('   ',end= '')    
    print("")
    

a = ~4
b = a + 4
print(b)


print("abc.DEF".capitalize())


l = [1,2,3,4,5]
value=[x&1 for x in l]
print(value)