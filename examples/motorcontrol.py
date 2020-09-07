import time
import sys
import RPi.GPIO as GPIO

enablePin = 17
inputPin1 = 27
inputPin2 = 22
global currentSpeed = 50


GPIO.setmode(GPIO.BCM)
GPIO.setup(enablePin, GPIO.OUT)
GPIO.setup(inputPin1, GPIO.OUT)
GPIO.setup(inputPin2, GPIO.OUT)
pmw = GPIO.PWM(enablePin, 1000)
pmw.start(currentSpeed)


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

def stop():
  GPIO.output(enablePin, False)
  GPIO.output(inputPin1, False)
  GPIO.output(inputPin2, False)

def increaseSpeed():
  currentSpeed = currentSpeed + 10
  pmw.ChangeDutyCycle(currentSpeed)

def decreaseSpeed():
  currentSpeed = currentSpeed - 10
  pmw.ChangeDutyCycle(currentSpeed)


try:
  while True:
    command = input('Choose a direction (f)orward,(b)ackward,(s)top,(i)ncrease Speed,(d)ecrease Speed: ')
    if command == "f":
      forward()
    if command == "b":
      backward()
    if command == "s":
      stop()
    if command == "i":
      increaseSpeed()
    if command == "d":
      decreaseSpeed()


except KeyboardInterrupt:
  GPIO.cleanup()


