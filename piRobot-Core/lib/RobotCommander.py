from lib.Robot import Robot
import json;

class RobotCommander:

  def __init__(self):
    self.robot = Robot()

  def handleAPICommand(self, commandJson):
    jsonStream = json.loads(commandJson)
    command = jsonStream['command']
    if command == "mf":
      self.robot.moveForward()
    if command == "mb":
      self.robot.moveBackward()
    if command == "ms":
      self.robot.moveStop()
    if command == "ml":
      self.robot.moveLeft()
    if command == "mr":
      self.robot.moveRight()

  def handleCLICommand(self, command):
    if command == "f":
      self.robot.moveForward()
    if command == "b":
      self.robot.moveBackward()
    if command == "l":
      self.robot.moveLeft()
   # if command == "r":
   #   vehicle.right()
   # if command == "s":
   #   vehicle.stop()
   # if command == "d":
   #   vehicle.decreaseSpeed()
   # if command == "i":
   #   vehicle.increaseSpeed()