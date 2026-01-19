from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        print("abstract method")


class rectangle(shape):
    def area(self):
        print("area method implementation")

r=rectangle()
r.area()
r.display()
