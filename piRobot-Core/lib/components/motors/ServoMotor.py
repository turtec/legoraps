import time
import pigpio

class ServoMotor:

    # Initializer / Instance Attributes
    def __init__(self, servoPin, GPIO):
        #self.GPIO = GPIO
        #self.GPIO.setmode(self.GPIO.BCM)
        self.servoPIN = servoPin
        self.pi = pigpio.pi()
        self.pi.set_mode(self.servoPIN, pigpio.OUTPUT)

    # most left
    def left(self):
       print('servo forward')
       goal = 1000
       self.move(goal)
   
    # most right   
    def right(self):
       print('servo backward')
       goal = 2500
       self.move(goal)

    # middle position
    def middle(self):
       print('servo backward')
       goal = 2000
       self.move(goal)
    
    def move(self, goal):
       currentposition = self.pi.get_servo_pulsewidth(self.servoPIN)
       if currentposition < goal:
         stepdirection = 10
       else:
         stepdirection = -10
       for x in range(currentposition, goal, stepdirection):
         self.pi.set_servo_pulsewidth(self.servoPIN, x)
         time.sleep(0.01)



