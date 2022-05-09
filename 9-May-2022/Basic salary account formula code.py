Basic_Salary = input("Enter Basic Salary :")

DA = (Basic_Salary * 40) / 100
HRA = (Basic_Salary * 20) / 100
Gross_Salary = Basic_Salary + DA + HRA

print "\n\nDearness Allowance 40 % of Basic Salary :" , DA
print "House Rent 20 % of Basic Salary :" , HRA
print "Gross Salary :" , Gross_Salary