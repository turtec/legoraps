from lib.composedcomponents.Vehicle import Vehicle
from lib.composedcomponents.CamPanTilt import CamPanTilt
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    # Error handling
    import FakeRPi.GPIO as GPIO

class Robot:

  def __init__(self):
    self.vehicle = Vehicle(17,27,22,13,6,5,GPIO)
    #self, servoPin, stepPinA1, stepPinA2, stepPinB1, stepPinB2, GPIO
    self.camPanTilt = CamPanTilt(16,1,1,1,1,GPIO)

  def camUp(self):
   self.camPanTilt.up()

  def camDown(self):
   print("camdown")
   self.camPanTilt.down()

  def camMiddle(self):
   print("camdown")
   self.camPanTilt.front()


  def moveRight(self):
    self.vehicle.right()

  def moveLeft(self):
    self.vehicle.left()

  def moveForward(self):
    self.vehicle.forward()

  def moveBackward(self):
    self.vehicle.backward()

  def increaseSpeed(self):
    self.vehicle.increaseSpeed()

  def decreaseSpeed(self):
    self.vehicle.decreaseSpeed()

  def moveStop(self):
    self.vehicle.stop()




