from DcMotor import DcMotor 

class Vehicle:

  # Initializer / Instance Attributes
  def __init__(self, enablePinLeft, inputPin1Left, inputPin2Left,enablePinRight,inputPin1Right,inputPin2Right):
      self.enablePinLeft = enablePinLeft
      self.inputPin1Left = inputPin1Left
      self.inputPin2Left = inputPin2Left
      self.enablePinRight = enablePinRight
      self.inputPin1Right = inputPin1Right
      self.inputPin2Right = inputPin2Right
      self.rightDc = DcMotor('right',enablePinRight,inputPin1Right,inputPin2Right)
      self.leftDc = DcMotor('left',enablePinLeft,inputPin1Left,inputPin2Left)

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
      self.rightDc.stop()
      self.leftDc.forward()
      print('#############')

  def right(self):
      print('right')
      self.rightDc.forward()
      self.leftDc.stop()
      print('#############')
