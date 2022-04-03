class  Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getstatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available  in the train are {self.seats}")

    def fareInfo(self):
        print(f"The price of the tickets is : {self.fare}")

intercity = Train("Intercity Express: 14015",180,350)
intercity.getstatus()
intercity.fareInfo()
