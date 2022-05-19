num = int(input("Enter the number that you want to divide:"))
listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num% number == 0:

        divisorList.append(number)
print(divisorList)

