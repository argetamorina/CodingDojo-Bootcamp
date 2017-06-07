class Bike(object):
    """docstring for ."""
    def __init__(self, price, max_speed, miles = 0):
        # super(, self).__init__()
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print "The price for this bike is {}, it has a maximum speed of {} and miles of {}".format(self.price,self.max_speed, self.miles)
        return self
    def ride(self):
        print "Riding... Miles: {}".format(self.miles + 10)
        return self
    def reverse(self):
        print "Riding... Miles: {}".format(self.miles + 5)
        return self

bike = Bike(200, "25mph", 2050)
bike.displayInfo().ride().reverse()

print ""
bike2 = Bike(900, "235mph", 4050)
bike2.ride().reverse().displayInfo()
