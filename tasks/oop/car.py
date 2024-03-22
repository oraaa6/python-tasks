from vehicle import Vehicle

class Car(Vehicle): # inheritance - Car inherit attributes from Vehicle
        
    def brag(self):
        print('Look how cool my car is!')
        
car1 = Car()
car1.drive()
Car.top_speed = 200
car1.add_warning('New Warning')
print(car1.get_warnings()) # ['New Warning'] 

car2 = Car(200)
car2.drive()
print(car2.get_warnings()) # [] - if we wouldn't overwrite constructor and leave warning as a attribute, here would also print ['New Warning']
print(car2) # it prints whole information, also address in memory
print(car2.__dict__) # print as a dictionary