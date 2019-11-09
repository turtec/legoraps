import time
import pigpio

class ServoMotor:

    # Initializer / Instance Attributes
    def __init__(self, servoPin, GPIO):
        self.GPIO = GPIO
        self.GPIO.setmode(self.GPIO.BCM)
        self.servoPIN = servoPin

    def left(self):
       print('servo forward')
       pi = pigpio.pi()
       pi.set_mode(self.servoPIN, pigpio.OUTPUT)
       sec = 1500
       pi.set_servo_pulsewidth(self.servoPIN, sec)
       time.sleep(1)

    def right(self):
       print('servo backward')
       pi = pigpio.pi()
       pi.set_mode(self.servoPIN, pigpio.OUTPUT)
       sec = 2500
       pi.set_servo_pulsewidth(self.servoPIN, sec)
       time.sleep(1)

    def middle(self):
       print('servo backward')
       pi = pigpio.pi()
       pi.set_mode(self.servoPIN, pigpio.OUTPUT)
       sec = 2000
       pi.set_servo_pulsewidth(self.servoPIN, sec)
       time.sleep(1)

