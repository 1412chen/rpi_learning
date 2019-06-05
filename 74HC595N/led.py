import RPi.GPIO as GPIO
import time

SRCLK = 21
RCLK = 20
SER = 16

# init
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(SRCLK, GPIO.OUT)
GPIO.setup(RCLK, GPIO.OUT)
GPIO.setup(SER, GPIO.OUT)
GPIO.output(SER, GPIO.LOW)
GPIO.output(SRCLK, GPIO.LOW)
GPIO.output(RCLK, GPIO.LOW)

# mode 1: all 1
GPIO.output(SER, GPIO.HIGH)
for i in range(8):
  GPIO.output(SRCLK, GPIO.HIGH)
  GPIO.output(SRCLK, GPIO.LOW)
GPIO.output(RCLK, GPIO.HIGH)
GPIO.output(RCLK, GPIO.LOW)
time.sleep(1)

# mode 2: all 0
GPIO.output(SER, GPIO.LOW)
for i in range(8):
  GPIO.output(SRCLK, GPIO.HIGH)
  GPIO.output(SRCLK, GPIO.LOW)
GPIO.output(RCLK, GPIO.HIGH)
GPIO.output(RCLK, GPIO.LOW)
time.sleep(1)

# mode 3: A ~ G to 1 sequentially
GPIO.output(SER, GPIO.HIGH)
for i in range(8):
  GPIO.output(SRCLK, GPIO.HIGH)
  GPIO.output(SRCLK, GPIO.LOW)
  GPIO.output(RCLK, GPIO.HIGH)
  GPIO.output(RCLK, GPIO.LOW)
  time.sleep(0.5)

# mode 4: A ~ G to 0 sequentially
GPIO.output(SER, GPIO.LOW)
for i in range(8):
  GPIO.output(SRCLK, GPIO.HIGH)
  GPIO.output(SRCLK, GPIO.LOW)
  GPIO.output(RCLK, GPIO.HIGH)
  GPIO.output(RCLK, GPIO.LOW)
  time.sleep(0.5)
 
# mode 5: 0 & 1 crossing sequence
mode = GPIO.HIGH
for i in range(8):
  GPIO.output(SER, mode)
  GPIO.output(SRCLK, GPIO.HIGH)
  GPIO.output(SRCLK, GPIO.LOW)
  GPIO.output(RCLK, GPIO.HIGH)
  GPIO.output(RCLK, GPIO.LOW)
  GPIO.output(RCLK, GPIO.HIGH)
  GPIO.output(RCLK, GPIO.LOW)
  if mode == GPIO.HIGH:
    mode = GPIO.LOW
  else:
    mode = GPIO.HIGH
  time.sleep(0.5)
GPIO.output(SER, GPIO.LOW)
for i in range(8):
  GPIO.output(SRCLK, GPIO.HIGH)
  GPIO.output(SRCLK, GPIO.LOW)
  GPIO.output(RCLK, GPIO.HIGH)
  GPIO.output(RCLK, GPIO.LOW)
  time.sleep(0.5)
