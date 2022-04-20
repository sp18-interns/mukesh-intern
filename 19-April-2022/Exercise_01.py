# import math
# r = 6
# h = 10

# def combine (digits):
#     return digits[0]*100 + digits[1]*10 + digits[2]

# d = (5 , 2, 3)
# print(combine(d))

# def circle(radius):
#     # compute and return area of circle
#     return math.pi * radius**2




# print(circle(2))    

# class Fraction(object):
#     """ A Number represents function as a fractions"""
#     def __init__(self, num, denom):
#         #num or denom are intergers
#         assert type(num) == int and type(denom) == int
#         self.num = num
#         self.denom = denom
#     def __str__(self):
#         """Returns string representaions of str return str(self.num) + "/" + str(self.demon)"""
#         return str(self.num) + "/" + str(self.denom)
#     def __add__(self,other):
#         top = self.num*other.denom + self.denom*other.num
#         bott = self.denom*other.denom
#         return Fraction(top,bott)
#     def __sub__(self,other):
#         top = self.num*other.denom - self.denom*other.num
#         bott = self.denom*other.denom
#         return Fraction(top, bott)
#     def __float__(self):
#         return self.num/self.denom
#     def inverse(self):
#         return Fraction(self.denom ,self.num )

# a = Fraction(1, 4)
# b = Fraction(3, 4)
# c = a + b # c is a fraction object   
# print(c)
# print(float(c))
# print(Fraction.__float__(c))
# print(float(b.inverse()))



