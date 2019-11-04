from lib.Vehicle import Vehicle
import time
import sys

import importlib.util
try:
    print("use1")
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    print("use Fake")
    """
    import FakeRPi.GPIO as GPIO
    OR
    import FakeRPi.RPiO as RPiO
    """
    import FakeRPi.GPIO as GPIO

vehicle = Vehicle(1,2,3,4,5,6,GPIO)

def control(command):
  if command == "f":
    vehicle.forward()
  if command == "b":
    vehicle.backward()
  if command == "l":
    vehicle.left()
  if command == "r":
    vehicle.right()
  if command == "s":
    vehicle.stop()
  if command == "d":
    vehicle.decreaseSpeed()
  if command == "i":
    vehicle.increaseSpeed()

try:
  while True:
    val = input('Choose a direction (f)orward,(b)ackward,(l)eft,(r)ight,(s)top,(i)ncrease Speed,(d)ecrease Speed: ')
    control(val)

except KeyboardInterrupt:
  GPIO.cleanup()
  #stop()
  print('stopped')
  #
