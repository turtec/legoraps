#import RPi.GPIO as GPIOH

class DcMotor:

    # Initializer / Instance Attributes
    def __init__(self, name, enablePin, inputPin1, inputPin2, GPIO):
        self.name = name
        self.enablePin = enablePin
        self.inputPin1 = inputPin1
        self.inputPin2 = inputPin2
        self.GPIO = GPIO
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setup(enablePin, self.GPIO.OUT)
        self.GPIO.setup(inputPin1, self.GPIO.OUT)
        self.GPIO.setup(inputPin2, self.GPIO.OUT)

    def forward(self):
       print("{} is running forward".format(self.name))

    def backward(self):
       print ("{} is running backward".format(self.name))

    def stop(self):
       print ("{} is stopped".format(self.name))

    def increaseSpeed(self):
       print ("{} speed increased".format(self.name))

    def decreaseSpeed(self):
       print ("{} speed decreased".format(self.name))
