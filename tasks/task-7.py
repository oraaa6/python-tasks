#Follow the instructions explained in the problem video and try to implement a solution on your own. Compare it with my solution (video + downloadable files) thereafter.
#1) Create a Food class with a “name” and a “kind” attribute as well as a “describe() ” method (which prints “name” and “kind” in a sentence).
#2) Try turning describe()  from an instance method into a class and a static method. Change it back to an instance method thereafter.
#3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook() ” method to “Meat” and “clean() ” to “Fruit”.
#4) Overwrite a “dunder” method to be able to print your “Food” class.

# # WITH STATICMETHOD

class Food:
        
    @staticmethod # I cannot access to attribute from class, so I need to pass via arguments everything what need
    def describe_static_method(kind, name):
       print('Kind: {}, Name: {}'.format(kind, name))
        
    def __repr__(self):
        return str(self.__dict__)


Food.name = 'Banana' # this approach overwrite name/kind in class, so after each invoking Food.describe() results will be always the same
Food.kind = 'Fruit'
Food.describe('meat', 'Beef')


# # WITH CLASSMETHOD

class Food:
    name = 'X'
    kind = 'Y'
        
    @classmethod # I cannot access attributes from class for classmethod from constructor __init__. To have acces I need to add attribute outside __init__ 
    def describe(cls):
        print('Kind: {}, Name: {}'.format(cls.kind, cls.name))
        
    def __repr__(self):
        return str(self.__dict__)


Food.name = 'Banana' # this approach overwrite name/kind in class, so after each invoking Food.describe() results will be always the same
Food.kind = 'Fruit'
Food.describe()

# WITH INSTANCEMETHOD

class Food:
    
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        
    def describe(self):
       print('Kind: {}, Name: {}'.format(self.kind, self.name))
        
    def __repr__(self):
        return str(self.__dict__)
    

class Meat(Food):
     # If I don't set up own constructor, this class takes it from Food class
    def __init__(self, name):
        super().__init__(name, 'meat')
        
    def cook(self): 
        print('cooking!')
        
 
class Fruit(Food):
    def __init__(self, name):
        super().__init__(name, 'fruit')
        
    def clean(self):
        print('cleaning')
        
        
banana = Fruit('Banana')
banana.clean()
banana.describe()

pork = Meat(name='Pork')
pork.cook()
pork.describe()