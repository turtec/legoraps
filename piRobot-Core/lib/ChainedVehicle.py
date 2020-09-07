from lib.DcMotor import DcMotor

class ChainedVehicle:

  # Initializer / Instance Attributes
  def __init__(self, enablePinLeft, inputPin1Left, inputPin2Left,
      enablePinRight,inputPin1Right,inputPin2Right, GPIO):
     
      self.enablePinLeft = enablePinLeft
      self.inputPin1Left = inputPin1Left
      self.inputPin2Left = inputPin2Left
      self.enablePinRight = enablePinRight
      self.inputPin1Right = inputPin1Right
      self.inputPin2Right = inputPin2Right
      self.rightDc = DcMotor('right',enablePinRight,inputPin1Right,inputPin2Right,GPIO)
      self.leftDc = DcMotor('left',enablePinLeft,inputPin1Left,inputPin2Left,GPIO)

  def speed(self):
      pass

  def forward(self):
      print('forward')
      self.rightDc.forward()
      self.leftDc.forward()
      print('#############')

  def backward(self):
      print('forward')
      self.rightDc.backward()
      self.leftDc.backward()
      print('#############')

  def stop(self):
      print('stop')
      self.rightDc.stop()
      self.leftDc.stop()
      print('#############')

  def left(self):
      print('left')
      self.rightDc.forward()
      self.leftDc.backward()
      print('#############')

  def right(self):
      print('right')
      self.rightDc.backward()
      self.leftDc.forward()
      print('#############')

  def increaseSpeed(self, number):
      print('increaseSpeed')
      self.rightDc.increaseSpeed(number)
      self.leftDc.increaseSpeed(number)
      print('#############')

  def decreaseSpeed(self, number):
      print('decreaseSpeed')
      self.rightDc.decreaseSpeed(number)
      self.leftDc.decreaseSpeed(number)
      print('#############')
