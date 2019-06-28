import RPi.GPIO as GPIO
import time

LED_PIN = 2

GPIO.setmode(GPIO.BCM)

def lightOff():
  GPIO.output(LED_PIN, GPIO.LOW)

def lightOn():
  GPIO.output(LED_PIN, GPIO.HIGH)

GPIO.setup(LED_PIN, GPIO.OUT)
lightOff()
time.sleep(1)
lightOn()
time.sleep(5)
lightOff()
