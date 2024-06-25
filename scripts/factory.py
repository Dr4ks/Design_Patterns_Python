from abc import ABC, abstractmethod

# Product interface
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

# Concrete ProductA
class Truck(Transport):
    def deliver(self):
        return "Delivering by truck"

# Concrete ProductB
class Ship(Transport):
    def deliver(self):
        return "Delivering by ship"

# Creator
class Logistic(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        return f"Planning delivery using {transport.deliver()}"

# Concrete CreatorA
class RoadLogistic(Logistic):
    def create_transport(self):
        return Truck()

# Concrete CreatorB
class SeaLogistic(Logistic):
    def create_transport(self):
        return Ship()

# Client code
def client_code(logistic):
    print(logistic.plan_delivery())

# Usage
road_logistic = RoadLogistic()
sea_logistic = SeaLogistic()

client_code(road_logistic)
client_code(sea_logistic)

## Output
# Planning delivery using Delivering by truck
# Planning delivery using Delivering by ship