from vehicle import Vehicle

class Bus(Vehicle):

    def  __init__(self, starting_top_speed=100):
        super().__init__(starting_top_speed) # super() - is parent constructor, which add access to the base class (Vehicle)
        self.passengers = [] # add new attribute, rest is inherited from vehicle

    def add_group(self, passengers):
        self.passengers.extend(passengers) # add new passengers to passengers list
        
bus1 = Bus(150)
bus1.add_warning('Test')
bus1.add_group(['Max', 'Manuel', 'Anna'])
print(bus1.passengers)
bus1.drive()