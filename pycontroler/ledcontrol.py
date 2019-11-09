from lib.LED import LED
import time
import sys

import importlib.util
try:
    print("use1")
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    print("use Fake")
    """
    import FakeRPi.GPIO as GPIO
    OR
    import FakeRPi.RPiO as RPiO
    """
    import FakeRPi.GPIO as GPIO

pin = 19
#GPIO.cleanup()
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(pin, GPIO.OUT)
#GPIO.output(pin, GPIO.HIGH)
led = LED(pin, GPIO)

def control(command):
  if command == "1":
    led.on()
  if command == "0":
    led.off()

try:
  while True:
    val = input('Choose a mode 1-on, 0-off: ')
    control(val)

except KeyboardInterrupt:
  GPIO.cleanup()
  #stop()
  print('stopped')
  #
