import RPi.GPIO as GPIO
import time

R_PIN = 2
G_PIN = 3
B_PIN = 4

# initial GPIO
def init():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.cleanup()

  GPIO.setup(R_PIN, GPIO.OUT)
  GPIO.setup(G_PIN, GPIO.OUT)
  GPIO.setup(B_PIN, GPIO.OUT)
  displayNone()

def displayNone():
  GPIO.output(R_PIN, GPIO.LOW)
  GPIO.output(G_PIN, GPIO.LOW)
  GPIO.output(B_PIN, GPIO.LOW)

def displayR():
  GPIO.output(R_PIN, GPIO.HIGH)
  GPIO.output(G_PIN, GPIO.LOW)
  GPIO.output(B_PIN, GPIO.LOW)

def displayG():
  GPIO.output(R_PIN, GPIO.LOW)
  GPIO.output(G_PIN, GPIO.HIGH)
  GPIO.output(B_PIN, GPIO.LOW)

def displayB():
  GPIO.output(R_PIN, GPIO.LOW)
  GPIO.output(G_PIN, GPIO.LOW)
  GPIO.output(B_PIN, GPIO.HIGH)

def displayRG():
  GPIO.output(R_PIN, GPIO.HIGH)
  GPIO.output(G_PIN, GPIO.HIGH)
  GPIO.output(B_PIN, GPIO.LOW)

def displayRB():
  GPIO.output(R_PIN, GPIO.HIGH)
  GPIO.output(G_PIN, GPIO.LOW)
  GPIO.output(B_PIN, GPIO.HIGH)

def displayGB():
  GPIO.output(R_PIN, GPIO.LOW)
  GPIO.output(G_PIN, GPIO.HIGH)
  GPIO.output(B_PIN, GPIO.HIGH)

def displayRGB():
  GPIO.output(R_PIN, GPIO.HIGH)
  GPIO.output(G_PIN, GPIO.HIGH)
  GPIO.output(B_PIN, GPIO.HIGH)

init()
displayR()
time.sleep(1)
displayG()
time.sleep(1)
displayB()
time.sleep(1)
displayRG()
time.sleep(1)
displayRB()
time.sleep(1)
displayGB()
time.sleep(1)
displayRGB()
time.sleep(1)
displayNone()
