import time
import sys
import RPi.GPIO as GPIO

enablePin = 17
inputPin1 = 27
inputPin2 = 22
        
def control(command):
  if command == "f":
    forward()
  if command == "b":
    backward()
  if command == "s":
    stop()

def forward():
  GPIO.output(enablePin, True)
  GPIO.output(inputPin1, True)
  GPIO.output(inputPin2, False)

def backward():
  GPIO.output(enablePin, True)
  GPIO.output(inputPin1, False)
  GPIO.output(inputPin2, True)

def stop(self):
  GPIO.output(enablePin, False)
  GPIO.output(inputPin1, False)
  GPIO.output(inputPin2, False)

try:
  while True:
    command = input('Choose a direction (f)orward,(b)ackward,(s)top,(i)ncrease Speed,(d)ecrease Speed: ')
    if command == "f":
      forward()
    if command == "b":
      backward()
    if command == "s":
      stop()

except KeyboardInterrupt:
  GPIO.cleanup()


