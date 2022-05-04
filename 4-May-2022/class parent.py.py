# from re import L
# from urllib.parse import ParseResultBytes


# class Animal(object):
#     pass

# class Dog(Animal):
#     def __init__(self,name):
#         self.name = name

# class Cat(Animal):
    
#     def __init__(self, name):
#         self.name = name

# class Person(object):

#     def __init__(self,name):

#         self.name = name

#     ## Person has-a pet of some kind

#         self.pet = None

# class Employee(Person):

#     def __init__(self,name,salary):

#         super(Employee, self).__init__(name)

#         self.salary = salary
# ## ??
# class Fish(object):
#     pass
# ##??
# class Salmon(Fish):
#     pass

# class Halibut(Fish):
#     pass
# #rover is-a Dog
# rover = Dog("Rover")

# ##??
# satan = Cat("Satan")

# mary = Person("Mary")

# mary.pet = satan

# frank = Employme("Frank", 45000)

# frank.pet = rover

# flipper = Fish()

# crouse = Salmon()

# harry = Halibut()


class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()