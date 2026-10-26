from abc import ABC,abstractmethod
class SmartDevice(ABC):
    def show_device(self,name):
        print("Device name:",name)
    @abstractmethod
    def turn_on(self):
        pass


class SmartLight(SmartDevice):
    def turn_on(self):
        print("Successfully turned on smart light")

class SmartFan(SmartDevice):
    def turn_on(self):
        print("Successfully turned on smart fan")

class SmartSpeaker(SmartDevice):
    def turn_on(self):
        print("Successfully turned on smart Speaker")

light = SmartLight()
light.show_device("living room light")
light.turn_on()

fan = SmartFan()
fan.show_device("bedroom fan")
fan.turn_on()

speaker = SmartSpeaker()
speaker.show_device("music speaker")
speaker.turn_on()

class SecurityCamera:
    def check_status(self):
        print("security camera is recording")
class DoorLock:
    def check_status(self):
        print("Door Lock is secure")

devices = [SecurityCamera(),DoorLock()]

print("")
print("===== SMART DEVICE STATUS =====")

for device in devices:
    device.check_status()

print("="*31)
