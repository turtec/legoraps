from Vehicle import Vehicle 
import time

vehicle = Vehicle(1,2,3,4,5,6)

def control(command):
  if command == "f":
    vehicle.forward()
  if command == "b":
    vehicle.backward()
  if command == "l":
    vehicle.left()
  if command == "r":
    vehicle.right()
  if command == "s":
    vehicle.stop()

try:
  while True:
    val = input('Choose a direction (f)orward,(b)ackward,(l)eft,(r)ight,(s)top: ')
    control(val)
 
except KeyboardInterrupt:
  stop()
  print('stopped')
  #GPIO.cleanup()
