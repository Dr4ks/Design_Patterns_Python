from abc import ABC, abstractmethod
from typing import List

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, price: float):
        pass

# Observable
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self, price: float):
        pass

# Concrete Observer
class StockObserver(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, price: float):
        print(f"{self.name} - Price updated: {price}")

# Concrete Observable
class Stock(Subject):
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.price = 0.0
        self.observers: List[Observer] = []

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self, price: float):
        for observer in self.observers:
            observer.update(price)

    def set_price(self, price: float):
        self.price = price
        self.notify_observers(self.price)

# Client code
def client_code():
    stock = Stock("AAPL")

    observer1 = StockObserver("Observer 1")
    observer2 = StockObserver("Observer 2")

    stock.register_observer(observer1)
    stock.register_observer(observer2)

    stock.set_price(150.0)
    stock.set_price(155.0)

# Usage
client_code()


## Output
# Observer 1 - Price updated: 150.0
# Observer 2 - Price updated: 150.0
# Observer 1 - Price updated: 155.0
# Observer 2 - Price updated: 155.0