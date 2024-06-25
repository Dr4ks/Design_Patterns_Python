from abc import ABC, abstractmethod

# Receiver
class Light:
    def turn_on(self):
        print("The light is on")

    def turn_off(self):
        print("The light is off")

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete Command for turning on the light
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

# Concrete Command for turning off the light
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

# Client code
def client_code():
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    remote = RemoteControl()

    remote.set_command(light_on)
    print("Client: Turning the light on.")
    remote.press_button()

    remote.set_command(light_off)
    print("Client: Turning the light off.")
    remote.press_button()

# Usage
client_code()

## Output
# Client: Turning the light on.
# The light is on
# Client: Turning the light off.
# The light is off
