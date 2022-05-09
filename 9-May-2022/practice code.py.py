import datetime
x = datetime.datetime(2022,5,9)
print(x)


class Salary(object):

    def calculate_gross_salary(basic_salary):
        hra = 0 #House Rent allowance
        da = 0  #Dearness allowance

class Employee:

    def __init__(self,Name,Post,hours_worked,wage,):
        self.Name = Name
        self.post = Post
        self.hours_worked = hours_worked
        self.wage = wage

    def salary(self):
        
    # if self.hours_worked > 35:
    #     return f{self.wage}
    def per_day_wage(self):
        return monthly_income / total_no_of_days_in_month
    def __str__(self):
        print({self.Name} , {self.Post} , {self.wage()})

e1 = Employee(Yujitesh, Management,4000 ) 
print(e1)                                              

def name_of_function(name):
    print("HEllo" + name)

name_of_function("Rossy")

def add_function(num1,num2):
    return num1+num2
result = add_function(4,5)
print(result)

def name_function():
    print("why are you so late")

name_function()

a = 400
b = 500
c = a + b
print(c)

def add(n1,n2):
    return n1+n2
result = add (20,30)
add(result)


  #points that are required

Basic_salary = input(int("enter the basic salary"))
DA = Basic salary*40 / 100
HRA = Basic salary*20 / 100
Gross_salary = Basic salary + DA + HRA






class Employee:
    Bare_minimum_working_hours = 40

    def __init__(self, name, post, hours_worked, wage_hour):
        self.name = name
        self.post = post
        self.hours_worked = hours_worked
        self.wage = wage_hour

    def salary(self):
        if self.hours_worked >= 40:
            return (f'Your CTC with OT is {40 * self.wage + (self.hours_worked - 40) * self.wage * 1.5}')
        else:
            return (f'The CTC is {self.hours_worked * self.wage}')


    def __str__(self):
        return f'{self.name}, {self.post}, {self.salary()}'  # if i don't use seperate {} then error

    def displayDetails(self):
        print("Name:", self.name, ", Designation:", self.post, ", Salary:", self.salary())


e1 = Employee("chittesh", "MO", 100000)
e2 = Employee("Ritesh", "C0", 100400)
print(e1)
print(e2)
print(f'Details of all employee: {e1} , {e2}')


class Employee:
    def __init__(self,first_name, last_name, birth_year,salary):
        self.first_name = first_name  
        self.last_name = last_name  
        self.birth_year = birth_year
        self.salary = salary

    def show(self):
         print(f'I am {self.first_name} {self.last_name} born in {self.birth_year}')