# mock_gpio.py
class GPIO:
    BCM = 'BCM'
    OUT = 'OUT'
    IN = 'IN'
    LOW = 0
    HIGH = 1

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

    @classmethod
    def output(cls, pin, state):
        print(f"Simulation de output: Pin {pin} -> {'HIGH' if state == GPIO.HIGH else 'LOW'}")

    @classmethod
    def input(cls, pin):
        # Simuler une valeur pour le capteur (peut être ajustée pour des tests)
        print(f"Simulation de input: Lecture de Pin {pin} -> {GPIO.LOW}")
        return GPIO.LOW  # Retourner une valeur par défaut, ici LOW

class MockPWM:
    def start(self, duty_cycle):
        print(f"Simulation de PWM start avec duty_cycle: {duty_cycle}")

    def ChangeDutyCycle(self, duty_cycle):
        print(f"Simulation de changement de duty_cycle: {duty_cycle}")

