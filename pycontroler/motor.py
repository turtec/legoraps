import RPi.GPIO as GPIO
import time
import pigpio


f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()


servoPIN = 23
pi = pigpio.pi()
pi.set_mode(servoPIN, pigpio.OUTPUT)
sec = 1700

#pi.set_servo_pulsewidth(servoPIN, sec)
#time.sleep(0.1)
#range 500 to 2500


for x in range(0, 50):
    sec=sec+20
    pi.set_servo_pulsewidth(servoPIN, sec)
    time.sleep(0.1)
    print(sec)

#f=open("status.txt","w")
#f.write('sec')
#f.close()


#pi.set_servo_pulsewidth(servoPIN, 550)

#time.sleep(0.1)

#pi.set_servo_pulsewidth(servoPIN, 600)

#time.sleep(0.1)

pi.set_servo_pulsewidth(servoPIN, 0)

#pi.set_servo_pulsewidth(servoPIN, 500)


#GPIO.setmode(GPIO.BCM)
#GPIO.setup(servoPIN, GPIO.OUT)

#p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
#p.start(0) # Initialization
#try:
#  while True:
#    print('running')
#    p.ChangeDutyCycle(1.5)
#    time.sleep(1)
    
#except KeyboardInterrupt:
#  p.stop()
#  GPIO.cleanup()