class Abstraction:
    def __init__(self, implementor):
        self.implementor = implementor

    def operation(self):
        self.implementor.do_something()

class Implementor:
    def do_something(self):
        pass

class ConcreteImplementorA(Implementor):
    def do_something(self):
        print("Concrete Implementor A does something.")

class ConcreteImplementorB(Implementor):
    def do_something(self):
        print("Concrete Implementor B does something.")


implementor_a = ConcreteImplementorA()
abstraction = Abstraction(implementor_a)
abstraction.operation()


implementor_b = ConcreteImplementorB()
abstraction = Abstraction(implementor_b)
abstraction.operation()
