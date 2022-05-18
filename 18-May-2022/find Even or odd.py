from tokenize import Number


num = int(input("Enter the number:"))
Number = num%2
if Number > 0:
    print("You have pick ODD Number.")
else:
    print("You pick Even Number.")
    