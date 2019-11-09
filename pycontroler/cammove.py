from lib.CamPanTilt import CamPanTilt
import importlib.util

try:
    print("use1")
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    print("use Fake")
    import FakeRPi.GPIO as GPIO

#self, stepPinA1, stepPinA2, stepPinB1, stepPinB2,
#enablePinRight,inputPin1Right,inputPin2Right, GPIO
servoPin = 26
stepPinA1 = 1,
stepPinA2 = 2,
stepPinB1 = 3, 
stepPinB2 = 4,
camPanTilt = CamPanTilt(servoPin,stepPinA1, stepPinA2, stepPinB1, stepPinB2,GPIO)

def control(command):
  if command == "l":
    camPanTilt.left()
  if command == "r":
    camPanTilt.right()
  if command == "u":
    camPanTilt.up()
  if command == "d":
    camPanTilt.down()

try:
  while True:
    val = input('Choose a direction (u)p,(d)down,(l)eft,(r)ight: ')
    control(val)

except KeyboardInterrupt:
  GPIO.cleanup()
  print('stopped')
