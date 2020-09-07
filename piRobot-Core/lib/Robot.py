from lib.Vehicle import Vehicle
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    # Error handling
    import FakeRPi.GPIO as GPIO

class Robot:

  def __init__(self):
    self.vehicle = Vehicle(17,27,22,13,5,6,GPIO)

  def moveRight(self):
    self.vehicle.right()

  def moveLeft(self):
    self.vehicle.left()

  def moveForward(self):
    self.vehicle.forward()

  def moveBackward(self):
    self.vehicle.backward()

  def moveStop(self):
    self.vehicle.stop()




