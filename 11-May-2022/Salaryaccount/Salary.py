class Salary_account:
    def __init__(self, name='', wage=0.0, hours_worked=0.0, Basic_salary=0.0):
        self.name = name
        self.wage = wage
        self.hours_worked = hours_worked
        self.Basic_salary = Basic_salary

    def __str__(self):
        print(f'The name of the employee is {self.name} and the salary in which he hired is: {self.Basic_salary} ,the working hour of that employee is {self.hours_worked} ,Their daily wage is {self.wage}')

    def DA(self):  # Dearness allowance
        return (self.Basic_salary * 40) // 100

    def HRA(self):  # House Rent Allowance
        return (self.Basic_salary * 20) // 100

    def Gross_salary(self):
        return self.Basic_salary + self.DA() + self.HRA()

    def Daily_wage(self):
        return self.Basic_salary // 30

    def Incometax(self):
        return ((self.Basic_salary * 10) // 100)

    def ProvidentFund(self):
        return ((self.Basic_salary * 12) // 100)

    def Wageperhour(self):
        return self.Daily_wage() // 8

    def Overtime(self):
        return self.Wageperhour()

    print('**********************+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*************************>')