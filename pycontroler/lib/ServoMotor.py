import time
import pigpio

class ServoMotor:

    # Initializer / Instance Attributes
    def __init__(self, servoPin, GPIO):
        self.servoPin = enablePin
        self.GPIO = GPIO
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setup(enablePin, self.GPIO.OUT)
        self.GPIO.setup(inputPin1, self.GPIO.OUT)
        self.GPIO.setup(inputPin2, self.GPIO.OUT)

    def forward(self):
       pi = pigpio.pi()
       pi.set_mode(servoPIN, pigpio.OUTPUT)
       sec = 2000
       pi.set_servo_pulsewidth(servoPIN, sec)
       time.sleep(1)

    def backward(self):
       pi = pigpio.pi()
       pi.set_mode(servoPIN, pigpio.OUTPUT)
       sec = 1000
       pi.set_servo_pulsewidth(servoPIN, sec)
       time.sleep(1)


