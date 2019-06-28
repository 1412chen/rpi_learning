import RPi.GPIO as GPIO
import time

PIN = [2, 3, 4, 17]
MODE = {0: [0, 0, 0, 0],
        1: [1, 0, 0, 0],
        2: [1, 1, 0, 0],
        3: [0, 1, 0, 0],

        4: [0, 1, 1, 0],
        5: [0, 0, 1, 0],
        6: [0, 0, 1, 1],
        7: [0, 0, 0, 1],
        8: [1, 0, 0, 1]}

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
for pin in PIN:
  GPIO.setup(pin, GPIO.OUT)

def setMode(m):
  mode = MODE[m]
  for idx, pin in enumerate(PIN):
    GPIO.output(pin, mode[idx])
    #print(pin, mode)

setMode(0)
time.sleep(1)
for i in range(512):
  for i in [1, 2, 3, 4, 5, 6, 7, 8]:
    setMode(i)
    time.sleep(0.001)
setMode(0)
