import RPi.GPIO as GPIO
import time

SRCLK = 21
RCLK = 20
SER = 16
'''
LED A = pin 7 = QA
LED B = pin 6 = QB
LED C = pin 4 = QC
LED D = pin 2 = QD
LED E = pin 1 = QE
LED F = pin 9 = QF
LED G = pin 10 = QG
LED DP = pin 5 = QH
        pin 3/8 = VCC
'''

def init():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.cleanup()

  GPIO.setup(SRCLK, GPIO.OUT)
  GPIO.setup(RCLK, GPIO.OUT)
  GPIO.setup(SER, GPIO.OUT)
  GPIO.output(SER, GPIO.LOW)
  GPIO.output(SRCLK, GPIO.LOW)
  GPIO.output(RCLK, GPIO.LOW)

def display(frag):
  for v in frag:
    GPIO.output(SER, v)
    GPIO.output(SRCLK, GPIO.HIGH)
    GPIO.output(SRCLK, GPIO.LOW)
  GPIO.output(RCLK, GPIO.HIGH)
  GPIO.output(RCLK, GPIO.LOW)

num = {' ': [1, 1, 1, 1, 1, 1, 1, 1],
       '0': [1, 1, 0, 0, 0, 0, 0, 0],
       '1': [1, 1, 0, 0, 0, 0, 0, 0],
       '2': [1, 0, 1, 0, 0, 1, 0, 0],
       '3': [1, 0, 1, 1, 0, 0, 0, 0],
       '4': [1, 0, 0, 1, 1, 0, 0, 1],
       '5': [1, 0, 0, 1, 0, 0, 1, 0],
       '6': [1, 0, 0, 0, 0, 0, 1, 0],
       '7': [1, 1, 1, 1, 1, 0, 0, 0],
       '8': [1, 0, 0, 0, 0, 0, 0, 0],
       '9': [1, 0, 0, 1, 0, 0, 0, 0],
       'E': [1, 0, 0, 0, 0, 1, 1, 0],
       'F': [1, 0, 0, 0, 1, 1, 1, 0]}

init()
for i in "0123456789EF":
  display(num[i])
  time.sleep(1)

