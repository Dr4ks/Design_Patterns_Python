from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def operation(self):
        for child in self._children:
            child.operation()

class Leaf(Component):
    def operation(self):
        pass


root = Composite()
root.add(Leaf())
root.add(Leaf())

child = Composite()
child.add(Leaf())
child.add(Leaf())

root.add(child)

root.operation()
