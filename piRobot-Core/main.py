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
from lib.Vehicle import Vehicle

class Robot:

  def __init__(self):
    self.vehicle = Vehicle(21,16,20,17,27,22,GPIO)

  def receiveCommand(self, command):
    if command == "mf":
      self.vehicle.forward()
    if command == "mb":
      self.vehicle.backward()
    if command == "ms":
      self.vehicle.stop()
    if command == "ml":
      self.vehicle.left()
    if command == "mr":
      self.vehicle.right()

robot = Robot()

for line in sys.stdin:
    l = line
    print('line')
    print(line)
    robot.receiveCommand('mb')
    # Without this step the output may not be immediately available in node
    sys.stdout.flush()
