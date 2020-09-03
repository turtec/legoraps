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

class HelloRPC:

  # Initializer / Instance Attributes
  def __init__(self):
     self.counter = 0
     
  def fcCall(self, input):
      self.counter=self.counter+1
      return self.counter

vehicle = Vehicle(21,16,20,17,27,22,GPIO)

for line in sys.stdin:
   # l = json.loads(line)
    print(vehicle.forward())
    # Without this step the output may not be immediately available in node
    sys.stdout.flush()
