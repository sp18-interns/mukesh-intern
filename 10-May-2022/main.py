


'''
class Employee:
       def __init__(self,first_name, last_name, birth_year,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.salary = salary

       def show(self):
         print(f'I am {self.first_name} {self.last_name} born in {self.birth_year}')
'''


'''class BankAccount:
    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print(self.name, self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


a1 = BankAccount()
a1.set_details('Mike', 200)

a2 = BankAccount()
a2.set_details('Tom')

a1.display()
a2.display()

a1.withdraw(100)
a2.deposit(500)

a1.display()
a2.display()'''

'''Basic_Salary = input("Enter Basic Salary :")

DA = (Basic_Salary * 40) // 100
HRA = (Basic_Salary * 20) // 100
Gross_Salary =(Basic_Salary + DA + HRA)

print('DA')
print('HRA')
print('Gross_Salary')'''


class Salary_account:
    def __init__(self, name='', wage=0.0, hours_worked=0.0, Basic_salary=0.0):
        self.name = name
        self.wage = wage
        self.hours_worked = hours_worked
        self.Basic_salary = Basic_salary

    def __str__(self):
        print(f'The name of the employee is {self.name} and the salary in which he hired is: {self.Basic_salary} ,the working hour of that employee is {self.hours_worked} ,Their daily wage is {self.wage}' )

    def DA(self): #Dearness allowance
        return ((self.Basic_salary * 40) // 100)

    def HRA(self): #House Rent Allowance
        return ((self.Basic_salary*20)//100)

    def Gross_salary(self):
        return self.Basic_salary + self.DA() + self.HRA()
    def Daily_wage(self):
        return self.Basic_salary//30

sal = Salary_account('Mukesh', 400.0, 8.0, 12000.0)
#print(sal)


print('Dearness Alownace of this employee :',sal.DA())
print('House Rent Allowance:',sal.HRA())
print('Total Gross Salary:',sal.Gross_salary())
print('Daily wage paid by the Company:',sal.Daily_wage())
#print(sal)

