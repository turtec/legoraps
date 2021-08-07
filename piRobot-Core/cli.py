import time
import sys
from lib.RobotCommander import RobotCommander

commander = RobotCommander()
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

    
try:
  while True:
    val = input('Choose a direction (f)orward,(b)ackward,(l)eft,(r)ight,(s)top,(i)ncrease Speed,(d)ecrease Speed: ')
    commander.handleCLICommand(val)

except KeyboardInterrupt:
  GPIO.cleanup()
  #stop()
  print('stopped')
  #
