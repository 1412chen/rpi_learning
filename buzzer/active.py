import RPi.GPIO as GPIO
import time

PIN = 2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(PIN, GPIO.OUT)

GPIO.output(PIN, GPIO.LOW)
GPIO.output(PIN, GPIO.HIGH)
time.sleep(1)
GPIO.output(PIN, GPIO.LOW)

