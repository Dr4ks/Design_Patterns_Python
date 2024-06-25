# Implementor Interface
class Device:
    def power_on(self):
        pass

    def power_off(self):
        pass

    def set_channel(self, number):
        pass

# Concrete Implementor 1
class TV(Device):
    def power_on(self):
        print("TV is now ON")

    def power_off(self):
        print("TV is now OFF")

    def set_channel(self, number):
        print(f"TV channel set to {number}")

# Concrete Implementor 2
class Radio(Device):
    def power_on(self):
        print("Radio is now ON")

    def power_off(self):
        print("Radio is now OFF")

    def set_channel(self, number):
        print(f"Radio channel set to {number}")

# Abstraction
class RemoteControl:
    def __init__(self, device):
        self.device = device

    def turn_on(self):
        self.device.power_on()

    def turn_off(self):
        self.device.power_off()

    def set_channel(self, number):
        self.device.set_channel(number)

# Refined Abstraction
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        print("Device is muted")

# Usage
tv = TV()
radio = Radio()

remote = RemoteControl(tv)
remote.turn_on()
remote.set_channel(5)
remote.turn_off()

advanced_remote = AdvancedRemoteControl(radio)
advanced_remote.turn_on()
advanced_remote.set_channel(10)
advanced_remote.mute()
advanced_remote.turn_off()

## Output
# TV is now ON
# TV channel set to 5
# TV is now OFF
# Radio is now ON
# Radio channel set to 10
# Device is muted
# Radio is now OFF