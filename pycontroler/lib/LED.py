
class LED:

    # Initializer / Instance Attributes
    def __init__(self, pin, GPIO):
        self.pin = pin
        self.GPIO = GPIO
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setup(pin, self.GPIO.OUT)

    def on(self):
       print ("LED is on")
       self.GPIO.output(self.pin,self.GPIO.HIGH)

    def off(self):
       print ("LED is off")
       self.GPIO.output(self.pin,self.GPIO.LOW)
