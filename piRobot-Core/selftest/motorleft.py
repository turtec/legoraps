from lib.DcMotor import DcMotor
import time
import sys
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    # Error handling
    import FakeRPi.GPIO as GPIO

EnableA = 21
Input1 = 16
Input2 = 20
    
#EnableA = 26
#Input1 = 19
#Input2 = 13
    
def control(command):
  if command == "f":
    motor.forward()
  if command == "b":
    motor.backward()
  if command == "s":
    motor.stop()

motor = DcMotor('left',EnableA, Input1, Input2,GPIO)




try:
  while True:
    val = input('Choose a direction (f)orward,(b)ackward,(s)top,(i)ncrease Speed,(d)ecrease Speed: ')
    control(val)

except KeyboardInterrupt:
  GPIO.cleanup()
  #stop()
  print('stopped')
  #



