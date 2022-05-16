class Salary_account:
    def __init__(self, name='', wage=0.0, hours_worked=0.0, Basic_salary=0.0):
        self.name = name
        self.wage = wage
        self.hours_worked = hours_worked
        self.Basic_salary = Basic_salary

    def __str__(self):
        print(f'The name of the employee is {self.name} and the salary in which he hired is: {self.Basic_salary} ,the working hour of that employee is {self.hours_worked} ,Their daily wage is {self.wage}')

    def da(self):  # Dearness allowance
        return (self.Basic_salary * 40) // 100

    def hra(self):  # House Rent Allowance
        return (self.Basic_salary * 20) // 100

    def gross_salary(self):
        return self.Basic_salary + self.da() + self.hra()

    def daily_wage(self):
        return self.Basic_salary // 30

    def incometax(self):
        return ((self.Basic_salary * 10) // 100)

    def providentFund(self):
        return ((self.Basic_salary * 12) // 100)

    def wageperhour(self):
        return self.daily_wage() // 8

    def overtime(self):
        return (self.wageperhour() * 2) + self.gross_salary()

    print('**********************+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*************************>')