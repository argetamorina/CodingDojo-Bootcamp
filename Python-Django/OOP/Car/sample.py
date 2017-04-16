class Car(object):
    def __init__(self,  price, speed, fuel, mileage):
        # super(, self).__init__()
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.12
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
            print self.tax
    def display_all(self):
        print "Price: {} \nSpeed: {} \nFuel: {} \nMileage: {} \nTax:  {}\n".format(self.price, self.speed, self.fuel, self.mileage, self.tax)

car = Car(10005, "35mph", "Full", "105mpg")
car.display_all()
car2 = Car(2003, "105mph", " Not Full", "195mpg")
car2.display_all()
car3 = Car(2004, "35mph", "Full", "1205mpg")
car3.display_all()
car4 = Car(2005, "35mph", " Not Full", "1405mpg")
car4.display_all()
car5 = Car(20036, "35mph", "Full", "505mpg")
car5.display_all()
car6 = Car(20067, "35mph", "Full", "305mpg")
car6.display_all()
