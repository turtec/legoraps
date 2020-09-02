from lib.ServoMotor import ServoMotor
from lib.StepMotor import StepMotor

class CamPanTilt:

  # Initializer / Instance Attributes
  def __init__(self, servoPin, stepPinA1, stepPinA2, stepPinB1, stepPinB2, GPIO):
      self.upDownDriver = ServoMotor(servoPin,GPIO)
      self.leftRightDriver = StepMotor('stepcam',stepPinA1,stepPinA2,stepPinB1,stepPinB2, GPIO)

  def up(self):
      print('up')
      self.upDownDriver.left()
      print('#############')


  def front(self):
      print('middle')
      self.upDownDriver.middle()
      print('#############')

  def down(self):
       print('down')
       self.upDownDriver.right()
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
