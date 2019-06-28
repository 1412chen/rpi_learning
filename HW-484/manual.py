import RPi.GPIO as GPIO
import time

PIN = 2

# initial GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(PIN, GPIO.IN)

while True:
  if GPIO.input(PIN):
    print(1)
  else:
    print(2)
  time.sleep(0.5)
