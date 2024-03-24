class Printable:
    def __repr__(self):
        return str(self.__dict__) # returns all attributes as a dictionary