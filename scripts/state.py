from abc import ABC, abstractmethod

# Context
class TrafficLight:
    def __init__(self):
        self._state = GreenLight()

    def change_state(self, state):
        self._state = state

    def request(self):
        self._state.handle()

# State
class LightState(ABC):
    @abstractmethod
    def handle(self):
        pass

# Concrete StateA
class GreenLight(LightState):
    def handle(self):
        print("Traffic Light is Green. Go!")

# Concrete StateB
class YellowLight(LightState):
    def handle(self):
        print("Traffic Light is Yellow. Prepare to stop.")

# Concrete StateC
class RedLight(LightState):
    def handle(self):
        print("Traffic Light is Red. Stop!")

# Client code
def client_code():
    traffic_light = TrafficLight()

    traffic_light.request()  
    traffic_light.change_state(YellowLight())
    traffic_light.request()  
    traffic_light.change_state(RedLight())
    traffic_light.request()  

# Usage
client_code()


## Output
# Traffic Light is Green. Go!
# Traffic Light is Yellow. Prepare to stop.
# Traffic Light is Red. Stop!

