class DcMotor:

    # Initializer / Instance Attributes
    def __init__(self, name, enablePin, inputPin1, inputPin2, GPIO):
        self.name = name
        self.enablePin = enablePin
        self.inputPin1 = inputPin1
        self.inputPin2 = inputPin2
        self.GPIO = GPIO
        self.currentSpeed = 50
        self.GPIO.setmode(self.GPIO.BCM)
        self.pwm = GPIO.PWM(enablePin,1000)
        self.GPIO.setup(enablePin, self.GPIO.OUT)
        self.GPIO.setup(inputPin1, self.GPIO.OUT)
        self.GPIO.setup(inputPin2, self.GPIO.OUT)
        self.pwm.start(0)
        self.pwm.ChangeDutyCycle(self.currentSpeed)

    def forward(self):
       print("{} is running forward".format(self.name))
       self.GPIO.output(self.enablePin, True)
       self.GPIO.output(self.inputPin1, True)
       self.GPIO.output(self.inputPin2, False)

    def backward(self):
       print ("{} is running backward".format(self.name))
       self.GPIO.output(self.enablePin, True)
       self.GPIO.output(self.inputPin1, False)
       self.GPIO.output(self.inputPin2, True)

    def stop(self):
       print ("{} is stopped".format(self.name))
       self.GPIO.output(self.enablePin, False)
       self.GPIO.output(self.inputPin1, False)
       self.GPIO.output(self.inputPin2, False)

    def increaseSpeed(self):
       print ("{} speed increased".format(self.name))
   
       self.currentSpeed = self.currentSpeed + 10
       if self.currentSpeed <= 100:
         self.pwm.ChangeDutyCycle(self.currentSpeed)
       else:
         print('max speed 100')

    def decreaseSpeed(self):
       print ("{} speed decreased".format(self.name))
       self.currentSpeed = self.currentSpeed - 10
       if self.currentSpeed >= 0:
         self.pwm.ChangeDutyCycle(self.currentSpeed)
       else:
         print('min')
