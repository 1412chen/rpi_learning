import RPi.GPIO as GPIO
import time

PIN = 2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(PIN, GPIO.IN)

def callback(PIN):
  print("clicked")

GPIO.add_event_detect(PIN, GPIO.RISING, bouncetime=200, callback=callback)
#GPIO.add_event_callback(PIN, callback)

while True:
  time.sleep(10)
