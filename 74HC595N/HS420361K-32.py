import RPi.GPIO as GPIO
import time

SRCLK = 21
RCLK = 20
SER = 16
D1 = 2
D2 = 3
D3 = 4
D4 = 17
'''
LED A = pin 11 = QA
LED B = pin 7 = QB
LED C = pin 4 = QC
LED D = pin 2 = QD
LED E = pin 1 = QE
LED F = pin 10 = QF
LED G = pin 5 = QG
LED DP = pin 3 = QH
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

  GPIO.setup(D1, GPIO.OUT)
  GPIO.setup(D2, GPIO.OUT)
  GPIO.setup(D3, GPIO.OUT)
  GPIO.setup(D4, GPIO.OUT)
  GPIO.output(D1, GPIO.HIGH)
  GPIO.output(D2, GPIO.HIGH)
  GPIO.output(D3, GPIO.HIGH)
  GPIO.output(D4, GPIO.HIGH)

def display(frag):
  for v in frag:
    GPIO.output(SER, v)
    GPIO.output(SRCLK, GPIO.HIGH)
    GPIO.output(SRCLK, GPIO.LOW)
  GPIO.output(RCLK, GPIO.HIGH)
  GPIO.output(RCLK, GPIO.LOW)

def display4Digits(number):
  num = {' ': [0, 0, 0, 0, 0, 0, 0, 0],
       '0': [0, 0, 1, 1, 1, 1, 1, 1],
       '1': [0, 0, 0, 0, 0, 1, 1, 0],
       '2': [0, 1, 0, 1, 1, 0, 1, 1],
       '3': [0, 1, 0, 0, 1, 1, 1, 1],
       '4': [0, 1, 1, 0, 0, 1, 1, 0],
       '5': [0, 1, 1, 0, 1, 1, 0, 1],
       '6': [0, 1, 1, 1, 1, 1, 0, 1],
       '7': [0, 0, 0, 0, 0, 1, 1, 1],
       '8': [0, 1, 1, 1, 1, 1, 1, 1],
       '9': [0, 1, 1, 0, 1, 1, 1, 1],
       'E': [0, 1, 1, 1, 1, 0, 0, 1],
       'F': [0, 1, 1, 1, 0, 0, 0, 1]}
  digits = {1: D1, 2: D2, 3: D3, 4: D4}
  for t in range(100):
    for i in range(4):
      d = number[i]
      display(num[d])
      GPIO.output(digits[i+1], GPIO.LOW)
      time.sleep(0.01)
      GPIO.output(digits[i+1], GPIO.HIGH)

init()
display4Digits("89EF")
GPIO.cleanup()
