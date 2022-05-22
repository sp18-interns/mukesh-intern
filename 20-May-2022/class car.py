class Car():

    #pass
    def __init__(self,modelname,years,price):
        self.modelname = modelname
        self.years = years
        self.price = price
    def price_inc(self):
        self.price=(self.price*1.15)

class SuperCar(Car):
    def __init__(self,modelname,years,price,cc):
        super.__(modelname,years,price)
        self.cc= cc


BMW =SuperCar('X6',2020,1004000)
TATA = Car('punch',2022,1500000)

#--------------------------------------------------------------------------
BMW = Car()
TATA = Car()


BMW.modelname = 'X6'
BMW.years = 2020
BMW.price = 1004000

TATA.modelname = 'Punch'
TATA.year = 2020
TATA.price = 15000000

print(TATA.price)
print(TATA.years)
print(TATA.modelname)
BMW.CC = 6000
print(BMW.price)
print(BMW.years)
print(BMW.modelname)
#--------------------------------------------------------------------------------------------------------
BMW.cc   = 6000

print(BMW.__dict__)