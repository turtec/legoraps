class DcMotor:

    # Initializer / Instance Attributes
    def __init__(self, name, enablePin, inputPin1, inputPin2):
        self.name = name
        self.enablePin = enablePin
        self.inputPin1 = inputPin1
        self.inputPin2 = inputPin2
    
    def forward(self):
       print("{} is running forward".format(self.name))
     
    def backward(self):
       print ("{} is running backward".format(self.name))

    def stop(self):
       print ("{} is stopped".format(self.name))