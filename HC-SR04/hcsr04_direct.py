import RPi.GPIO as GPIO
import time

TRIG = 20
ECHO = 21

# init GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(TRIG, GPIO.LOW)

time.sleep(0.1)
GPIO.output(TRIG, GPIO.HIGH)
time.sleep(0.00001)
GPIO.output(TRIG, GPIO.LOW)

echo_count = 0
while GPIO.input(ECHO) == GPIO.LOW:
  if echo_count < 1000:
    echo_count += 1
    sonarStartTime = time.time()
  else:
    exit(1)
while GPIO.input(ECHO) == GPIO.HIGH:
  sonarEndTime = time.time()
distance = (sonarEndTime - sonarStartTime) / 58 * 1000000
print("{}".format(distance))

