# mock_gpio.py
class GPIO:
    BCM = None
    OUT = None

    @staticmethod
    def setmode(mode):
        print(f"Simulation de setmode: {mode}")

    @staticmethod
    def setup(pin, mode):
        print(f"Simulation de setup: Pin {pin}, Mode {mode}")

    @staticmethod
    def PWM(pin, frequency):
        print(f"Simulation de PWM: Pin {pin}, Fréquence {frequency}")
        return MockPWM()

    @staticmethod
    def cleanup():
        print("Simulation de cleanup")

class MockPWM:
    def start(self, duty_cycle):
        print(f"Simulation de PWM start avec duty_cycle: {duty_cycle}")

    def ChangeDutyCycle(self, duty_cycle):
        print(f"Simulation de changement de duty_cycle: {duty_cycle}")
