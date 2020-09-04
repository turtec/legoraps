import sys try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    # Error handling
    import FakeRPi.GPIO as GPIO
import json
from lib.RobotCommander import RobotCommander

commander = RobotCommander()

for line in sys.stdin:
    commander.handleAPICommand(line)
    # Without this step the output may not be immediately available in node
    sys.stdout.flush()
