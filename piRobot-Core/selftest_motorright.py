from lib.DcMotor import DcMotor
import time
import sys
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    # Error handling
    import FakeRPi.GPIO as GPIO

EnableA = 13
Input1 = 6
Input2 = 5
        
def control(command):
  if command == "f":
    motor.forward()
  if command == "b":
    motor.backward()
  if command == "s":
    motor.stop()

motor = DcMotor('right',EnableA, Input1, Input2, GPIO)




try:
  while True:
    val = input('Choose a direction (f)orward,(b)ackward,(s)top,(i)ncrease Speed,(d)ecrease Speed: ')
    control(val)

except KeyboardInterrupt:
  GPIO.cleanup()
  #stop()
  print('stopped')
  #



