from abc import ABC, abstractmethod 

class Figure(ABC):
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def area(self): pass

# inheritamce: class Deriver(Base)
class Rectangle(Figure):
    def __init__(self, name, width, height) -> None:
        # super() - reference to base class
        super().__init__(name)
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"{self.name}: {self.width}x{self.height}cm"

    def area(self):
        return self.width * self.height

    
f1 = Rectangle("Rectangle", 123, 88)

print(f1)

# error with creating Figure with abstract methods  
# figure = Figure("Figure")