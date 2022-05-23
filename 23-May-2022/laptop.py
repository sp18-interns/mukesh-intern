class Laptop:
    def __init__(self,brand,model_name,price):  #instance variables
        self.brand = brand
        self.name = model_name
        self.price = price

laptop1 = Laptop('Asus','TUF',58000)
print(laptop1.name)