from lib.ServoMotor import ServoMotor
from lib.StepMotor import StepMotor

class CamPanTilt:

  # Initializer / Instance Attributes
  def __init__(self, servoPin, stepPinA1, stepPinA2, stepPinB1, stepPinB2, GPIO):
      self.upDownDriver = ServoMotor('servoCam',servoPin)
      self.leftRightDriver = StepMotor('stepcam',stepPinA1,stepPinA2,stepPinB1,stepPinB2, GPIO)

  def up(self):
      print('up')
      self.upDownDriver.forward()
      print('#############')

  def down(self):
       print('down')
       self.upDownDriver.backward()
       print('#############')

  def left(self):
      print('left')
      #int(1) / 1000.0, int(128)
      self.leftRightDriver.forward(int(1) / 1000.0, int(128))
      print('#############')

  def right(self):
      print('right')
      self.leftRightDriver.backward(int(1) / 1000.0, int(128))
      print('#############')
