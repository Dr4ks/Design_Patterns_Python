from abc import ABC, abstractmethod

# Component
class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass

# Leaf
class Circle(Graphic):
    def draw(self):
        print("Circle")

# Leaf
class Square(Graphic):
    def draw(self):
        print("Square")

# Composite
class CompositeGraphic(Graphic):
    def __init__(self):
        self.children = [] # components

    def add(self, graphic):  # add component
        self.children.append(graphic)

    def remove(self, graphic):  # remove component
        self.children.remove(graphic)

    def draw(self):
        for child in self.children:
            child.draw()

# Client code
def client_code(graphic):
    graphic.draw()

# Usage
circle1 = Circle()
circle2 = Circle()
square1 = Square()

composite1 = CompositeGraphic()
composite1.add(circle1)
composite1.add(circle2)

composite2 = CompositeGraphic()
composite2.add(square1)
composite2.add(composite1)

print("Client: Drawing a composite graphic with nested components:")
client_code(composite2)

## Output
# Client: Drawing a composite graphic with nested components:
# Square
# Circle
# Circle
