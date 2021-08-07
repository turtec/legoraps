import RPi.GPIO as GPIO
import time

servoPIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p.start(2.5) # Initialisierung
print('start')
try:
  while True:
    print('run')
    p.ChangeDutyCycle(5)
    time.sleep(1000)
    p.ChangeDutyCycle(6)
    time.sleep(1000)
    
    
    
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()