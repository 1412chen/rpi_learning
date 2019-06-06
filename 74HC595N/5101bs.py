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
    if v:
      GPIO.output(SER, GPIO.HIGH)
    else:
      GPIO.output(SER, GPIO.LOW)
    GPIO.output(SRCLK, GPIO.HIGH)
    GPIO.output(SRCLK, GPIO.LOW)
  GPIO.output(RCLK, GPIO.HIGH)
  GPIO.output(RCLK, GPIO.LOW)

def display0():
  display([1, 1, 0, 0, 0, 0, 0, 0])

def display1():
  display([1, 1, 1, 1, 1, 0, 0, 1])

def display2():
  display([1, 0, 1, 0, 0, 1, 0, 0])

def display3():
  display([1, 0, 1, 1, 0, 0, 0, 0])

def display4():
  display([1, 0, 0, 1, 1, 0, 0, 1])

def display5():
  display([1, 0, 0, 1, 0, 0, 1, 0])

def display6():
  display([1, 0, 0, 0, 0, 0, 1, 0])

def display7():
  display([1, 1, 1, 1, 1, 0, 0, 0])

def display8():
  display([1, 0, 0, 0, 0, 0, 0, 0])

def display9():
  display([1, 0, 0, 1, 0, 0, 0, 0])

def displayE():
  display([1, 0, 0, 0, 0, 1, 1, 0])

def displayF():
  display([1, 0, 0, 0, 1, 1, 1, 0])

def displayNone():
  display([1, 1, 1, 1, 1, 1, 1, 1])


init()
display0()
time.sleep(1)
display1()
time.sleep(1)
display2()
time.sleep(1)
display3()
time.sleep(1)
display4()
time.sleep(1)
display5()
time.sleep(1)
display6()
time.sleep(1)
display7()
time.sleep(1)
display8()
time.sleep(1)
display9()
time.sleep(1)
displayE()
time.sleep(1)
displayF()
