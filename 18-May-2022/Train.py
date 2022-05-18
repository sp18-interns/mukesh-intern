class Railways:
    def __init__(self,max_speed,power):
        self.max_speed = max_speed
        self.power = power

modelX = Railways(105,250)
print(modelX.max_speed, modelX.power)


class Railways:
    pass

class Railways:

    def __init__(self, name,max_speed, power):
        self.name = name
        self.max_speed = max_speed
        self.power = power


    def seating_capacity(self, capacity):
        return f"the seating capacity of a {self.name} is {capacity} passengers"

class Local(Railways):
        pass
class Express(Railways):
        pass

class Railways:

    def __init__(self, name,max_speed, power):
        self.name = name
        self.max_speed = max_speed
        self.power = power


    def fare(self):
        return self.capacity * 500

class Local(Railways):
    pass

Raipur_local = Local("Raipur kutin",100,1000)

# python's built-in isinstance() function
print(isinstance(Raipur_Local, Railways))


