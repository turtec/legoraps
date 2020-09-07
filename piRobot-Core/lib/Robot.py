from lib.ChainedVehicle import ChainedVehicle
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    # Error handling
    import FakeRPi.GPIO as GPIO

class Robot:

  def __init__(self):
    self.vehicle = ChainedVehicle(17,27,22,13,6,5,GPIO)

  def moveRight(self):
    self.vehicle.right()

  def moveLeft(self):
    self.vehicle.left()

  def moveForward(self):
    self.vehicle.forward()

  def moveBackward(self):
    self.vehicle.backward()

  def increaseSpeed(self, number):
    self.vehicle.increaseSpeed(number)

  def decreaseSpeed(self, number):
    self.vehicle.decreaseSpeed(number)

  def moveStop(self):
    self.vehicle.stop()




