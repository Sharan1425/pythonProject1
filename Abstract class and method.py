from abc import ABC,abstractmethod
class my_class(ABC): # Abstract class
    @abstractmethod
    def hobby(self): # Abstract method
        pass
    @abstractmethod
    def age(self):
        pass

class Sharan(my_class):
    def hobby(self):
        print("i can use abstract method in sharan ")
class vishnu(Sharan):
    def age(self):
        print("18+")

v = vishnu()
v.hobby()
v.age()
