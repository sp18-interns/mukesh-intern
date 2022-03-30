class Employee:
    company = "spark"
    ecode = 121

class Freelancer:
    company = "JAXUX"
    level = 0

class Programmer(Employee,Freelancer):
    name = "HUZZY"

p = Programmer()
print(p.company)