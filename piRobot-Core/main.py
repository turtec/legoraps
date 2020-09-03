import sys 
import json
from lib.RobotCommander import RobotCommander

commander = RobotCommander()

for line in sys.stdin:
    commander.handleAPICommand(line)
    # Without this step the output may not be immediately available in node
    sys.stdout.flush()
