from lib.Vehicle import Vehicle
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

#EnableA = 21
#Input1 = 16
#Input2 = 20
    
#EnableA = 26
#Input1 = 19
#Input2 = 13
    
def control(command):
  if command == "f":
    robot.moveForward()


try:
  while True:
    val = input('Choose a direction (f)orward,(b)ackward,(l)eft,(r)ight,(s)top,(i)ncrease Speed,(d)ecrease Speed: ')
    commander.handleCLICommand(line)

except KeyboardInterrupt:
  GPIO.cleanup()
  #stop()
  print('stopped')
  #
