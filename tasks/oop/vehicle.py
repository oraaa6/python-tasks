class  Vehicle:
    def  __init__(self, starting_top_speed=100): # overwrite default constructor, constuctor is executes each time when we execute class, here: Car() and create new instance
        self.top_speed = 100 # because of that constructor, every instance receive own set
        self.__warnings = [] # __ <- tells python, that is private variable, what can't be access from outside, I can access it only from inside of class
        
    def __repr__(self): # we have to pass self 
        print('Printing...')
        return 'Top Speed: {}, Warnings: {}'.format(self.top_speed, len(self.__warnings)) # executes every time
    
    def add_warning(self, warning_test):
        if len(warning_test) > 0:
            self.__warnings.append(warning_test)
    
    def get_warnings(self):
        return self.__warnings
    
    def drive(self): # self - get access to the variables in class - ex top_speed of newly created attributes, 
        print('I am driving but certainly not faster than {}'.format(self.top_speed))