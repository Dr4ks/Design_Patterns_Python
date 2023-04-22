class Component:
    """Abstract base class for components"""

    def operation(self):
        pass

class ConcreteComponent(Component):
    """Concrete component class"""

    def operation(self):
        return "ConcreteComponent"

class Decorator(Component):
    """Base decorator class"""

    def __init__(self, component):
        self._component = component

    def operation(self):
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    """Concrete decorator class A"""

    def operation(self):
        return f"ConcreteDecoratorA({self._component.operation()})"

class ConcreteDecoratorB(Decorator):
    """Concrete decorator class B"""

    def operation(self):
        return f"ConcreteDecoratorB({self._component.operation()})"


if __name__ == "__main__":
    component = ConcreteComponent()
    decorator_a = ConcreteDecoratorA(component)
    decorator_b = ConcreteDecoratorB(decorator_a)

    print(component.operation()) 
    print(decorator_a.operation())  
    print(decorator_b.operation())  
