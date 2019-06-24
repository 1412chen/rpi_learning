import RPi.GPIO as GPIO
import time

DETECT_PIN = 3

# initial GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(DETECT_PIN, GPIO.IN)

def callback(PIN):
  print("detected")

GPIO.add_event_detect(DETECT_PIN, GPIO.BOTH, bouncetime=200)
GPIO.add_event_callback(DETECT_PIN, callback)


while True:
  time.sleep(10)
