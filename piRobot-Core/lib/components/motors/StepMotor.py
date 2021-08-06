import time

class StepMotor:

    # Initializer / Instance Attributes
    def __init__(self, name, inputPinA1, inputPinA2, inputPinB1, inputPinB2, GPIO):
        self.name = name
        self.inputPinA1 = inputPinA1
        self.inputPinA2 = inputPinA2
        self.inputPinB1 = inputPinB1
        self.inputPinB2 = inputPinB2
        self.GPIO = GPIO
        self.GPIO.setmode(GPIO.BCM)
        self.GPIO.setup(self.inputPinA1, GPIO.OUT)
        self.GPIO.setup(self.inputPinA2, GPIO.OUT)
        self.GPIO.setup(self.inputPinB1, GPIO.OUT)
        self.GPIO.setup(self.inputPinB2, GPIO.OUT)
        self.StepCount = 8
        self.SequenceArray = list(range(0, self.StepCount))
        self.SequenceArray[0] = [0,1,0,0]
        self.SequenceArray[1] = [0,1,0,1]
        self.SequenceArray[2] = [0,0,0,1]
        self.SequenceArray[3] = [1,0,0,1]
        self.SequenceArray[4] = [1,0,0,0]
        self.SequenceArray[5] = [1,0,1,0]
        self.SequenceArray[6] = [0,0,1,0]
        self.SequenceArray[7] = [0,1,1,0]


    def move(self, w1, w2, w3, w4):
        self.GPIO.output(self.inputPinA1, w1)
        self.GPIO.output(self.inputPinA2, w2)
        self.GPIO.output(self.inputPinB1, w3)
        self.GPIO.output(self.inputPinB2, w4)

    def forward(self, delay, steps):
        print("{} is running forward".format(self.name))
        for i in range(steps):
            for j in range(self.StepCount):
                self.move(self.SequenceArray[j][0], self.SequenceArray[j][1],
                self.SequenceArray[j][2], self.SequenceArray[j][3])
                time.sleep(delay)

    def backward(self, delay, steps):
        print ("{} is running backward".format(self.name))
        for i in range(steps):
            for j in reversed(range(self.StepCount)):
                self.move(self.SequenceArray[j][0], self.SequenceArray[j][1],
                self.SequenceArray[j][2], self.SequenceArray[j][3])
                time.sleep(delay)
