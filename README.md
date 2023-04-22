# Hi, I'm Dr4ks! 👋

## 🚀 About Me
I'm a Cyber Security student.

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sahib-humbatzada-42b082223/)
[![hackerrank](https://img.shields.io/badge/HackerRank-2EC866?style=for-the-badge&logo=hackerrank&logoColor=white)](https://www.hackerrank.com/Dr4ks)
[![tryhackme](https://img.shields.io/badge/tryhackme-1DB954?style=for-the-badge&logo=tryhackme&logoColor=white)](https://tryhackme.com/p/Dr4ks)
[![github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Dr4ks)

## 🛠 Skills
Python

# Design Patterns

Design patterns are proven solutions to recurring problems in software design. They are templates for solving similar problems in different contexts. Design patterns help in making software more modular, reusable, and maintainable.

## Practical Examples
These design patterns which we covered with examples.

- [Adapter](#adapter)
- [Bridge](#bridge)
- [Chain of Responsibility](#chain-of-responsibility)
- [Composite](#composite)
- [Decorator](#decorator)
- [Facade](#facade)
- [Factory](#factory)
- [Observer](#observer)
- [Proxy](#proxy)
- [Singleton](#singleton)
- [Strategy](#strategy)
- [Template-Method](#template-method)


## Adapter
The Adapter design pattern is a structural design pattern that allows incompatible interfaces to work together. It is useful when an existing class/interface cannot be modified to conform to the requirements of a new interface, or when there are multiple incompatible interfaces that need to be unified.

```python
class Adaptee: 
    def specific_request(self):
        return "Specific request."

class Target:
    def request(self):
        return "Generic request."

class Adapter(Target): 
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specific_request()

if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)

    print(adapter.request())

```

## Bridge
The Bridge design pattern is used to separate an abstraction from its implementation so that both can be changed independently. This pattern is useful when there are multiple implementations of a feature, and the client should be decoupled from the implementation details.

```python
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

```

## Chain of Responsibility
The Chain of Responsibility design pattern is a behavioral design pattern that allows a group of objects to handle a request, with each object either handling the request or passing it on to the next object in the chain.

```python
class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        handled = self._handle(request)

        if not handled:
            self._successor.handle_request(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass')


class ConcreteHandlerA(Handler):
    def _handle(self, request):
        if 0 < request <= 10:
            print(f'Request {request} handled by ConcreteHandlerA')
            return True


class ConcreteHandlerB(Handler):
    def _handle(self, request):
        if 10 < request <= 20:
            print(f'Request {request} handled by ConcreteHandlerB')
            return True


class ConcreteHandlerC(Handler):
    def _handle(self, request):
        if 20 < request <= 30:
            print(f'Request {request} handled by ConcreteHandlerC')
            return True


class DefaultHandler(Handler):
    def _handle(self, request):
        print(f'End of chain, no handler for {request}')
        return True

if __name__ == '__main__':
    handler_chain = ConcreteHandlerA(ConcreteHandlerB(ConcreteHandlerC(DefaultHandler())))
    requests = [2, 5, 14, 22, 18, 3, 35]

    for request in requests:
        handler_chain.handle_request(request)

```

## Composite
The Composite design pattern is a structural design pattern that lets you compose objects into a tree-like structure and work with the tree as if it was a singular object. The composite pattern allows you to create a hierarchy of objects where each object can be treated individually or as a part of a larger group.

```python
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

```

## Decorator
The Decorator design pattern is a structural pattern that allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class.

```python
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

```

## Facade
The Facade design pattern is a structural pattern that provides a simplified interface to a complex system of classes, interfaces, and objects. It is used to provide a single, unified interface to a set of interfaces in a subsystem, which makes the subsystem easier to use and understand.

```python
class TCPConnection:
    def connect(self):
        print("TCPConnection: connect")

class UDPConnection:
    def connect(self):
        print("UDPConnection: connect")

class HTTPConnection:
    def connect(self):
        print("HTTPConnection: connect")

class NetworkFacade:
    def __init__(self):
        self.tcp_connection = TCPConnection()
        self.udp_connection = UDPConnection()
        self.http_connection = HTTPConnection()

    def connect(self, protocol):
        if protocol == "TCP":
            self.tcp_connection.connect()
        elif protocol == "UDP":
            self.udp_connection.connect()
        elif protocol == "HTTP":
            self.http_connection.connect()

network = NetworkFacade()
network.connect("TCP")
network.connect("UDP")
network.connect("HTTP")

```

## Factory
The Factory design pattern is a creational pattern that provides an interface for creating objects in a super class, but allows subclasses to alter the type of objects that will be created. This pattern is useful when you want to create a family of related objects but you don't know exactly what kind of objects you need to create until runtime.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "Dog":
            return Dog()
        elif animal_type == "Cat":
            return Cat()
        else:
            raise Exception(f"Invalid animal type: {animal_type}")

animal_factory = AnimalFactory()

dog = animal_factory.create_animal("Dog")
print(dog.speak()) 

cat = animal_factory.create_animal("Cat")
print(cat.speak()) 
```

## Observer
The Observer design pattern is a behavioral design pattern that allows one-to-many communication between objects in a loosely coupled manner. In this pattern, an object (called the subject) maintains a list of its dependents (called observers) and notifies them automatically of any state changes, usually by calling one of their methods.

```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(*args, **kwargs)


class Observer:
    def update(self, *args, **kwargs):
        pass


class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
        self.notify(self._state)


class ConcreteObserverA(Observer):
    def update(self, state):
        print(f"Observer A received the state {state}")


class ConcreteObserverB(Observer):
    def update(self, state):
        print(f"Observer B received the state {state}")


subject = ConcreteSubject()
observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()

subject.attach(observer_a)
subject.attach(observer_b)

subject.state = "state 1"
subject.state = "state 2"

subject.detach(observer_b)

subject.state = "state 3"

```

## Proxy
The Proxy design pattern is a structural pattern that allows us to provide a surrogate or placeholder for another object to control access to it. It provides a way to add an extra level of indirection to support distributed, controlled, or intelligent access.

```python
class Subject:
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request.")

class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.")

        
if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    proxy.request()

```

## Singleton
The Singleton design pattern is a creational design pattern that restricts the instantiation of a class to one single instance and provides a global point of access to that instance. This can be useful when there should be only one instance of a class in the system, such as in the case of a configuration manager or a database connector.

```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def some_method(self):
        print("Some method")
    
s1 = Singleton()
s2 = Singleton()

print(s1 == s2) 

s1.some_method()  
s2.some_method()  


```

## Strategy
The Strategy design pattern is a behavioral design pattern that allows you to define a family of algorithms, encapsulate each one, and make them interchangeable at runtime. This pattern allows the algorithms to vary independently from the clients that use them. In this way, you can use this pattern to choose the algorithm that best suits a particular problem, context or situation at runtime.

```python
class SortStrategy:
    def sort(self, data):
        pass

class QuickSortStrategy(SortStrategy):
    def sort(self, data):
        print("Sorting using QuickSort")
        return sorted(data)

class MergeSortStrategy(SortStrategy):
    def sort(self, data):
        print("Sorting using MergeSort")
        return sorted(data)

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort_data(self, data):
        return self.strategy.sort(data)

data = [5, 3, 1, 4, 2]
strategy = QuickSortStrategy()
sorter = Sorter(strategy)
result = sorter.sort_data(data)
print(result)

strategy = MergeSortStrategy()
sorter = Sorter(strategy)
result = sorter.sort_data(data)
print(result)

```

## Template-Method
The Template Method design pattern is a behavioral pattern that allows you to define the skeleton of an algorithm in a superclass but lets you override specific steps of the algorithm in subclasses. This pattern is useful when you want to define a set of steps that can be customized to fit a particular use case.

```python
from abc import ABC, abstractmethod

class AlgorithmTemplate(ABC):

    def run(self):
        self.step_one()
        self.step_two()
        self.step_three()

    @abstractmethod
    def step_one(self):
        pass

    @abstractmethod
    def step_two(self):
        pass

    @abstractmethod
    def step_three(self):
        pass

class Algorithm1(AlgorithmTemplate):

    def step_one(self):
        print("Running step 1 for Algorithm 1")

    def step_two(self):
        print("Running step 2 for Algorithm 1")

    def step_three(self):
        print("Running step 3 for Algorithm 1")

class Algorithm2(AlgorithmTemplate):

    def step_one(self):
        print("Running step 1 for Algorithm 2")

    def step_two(self):
        print("Running step 2 for Algorithm 2")

    def step_three(self):
        print("Running step 3 for Algorithm 2")

algorithm1 = Algorithm1()
algorithm1.run()

algorithm2 = Algorithm2()
algorithm2.run()

```


## Authors

- [@dr4ks](https://www.github.com/Dr4ks)

