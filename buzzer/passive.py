import RPi.GPIO as GPIO
import time

PIN = 2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(PIN, GPIO.OUT)

def buzz(freq, leng):
  delayValue = 0.5/freq
  cycle = freq*leng/1000
  for i in range(cycle):
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(delayValue)
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(delayValue)

tone = [262, 294, 330, 349, 392, 440, 494]
duration = 1000/12
for t in tone:
  buzz(t, duration)
  time.sleep(0.01)
