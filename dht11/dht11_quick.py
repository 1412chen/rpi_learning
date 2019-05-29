import RPi.GPIO as GPIO
import time

PIN = 4

# initial GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# step a, b
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.LOW)
time.sleep(0.0181)
GPIO.output(PIN, GPIO.HIGH)

# step c, d
GPIO.setup(PIN, GPIO.IN, GPIO.PUD_UP)
while GPIO.input(PIN) == GPIO.LOW:
  continue
while GPIO.input(PIN) == GPIO.HIGH:
  continue

# step e
bits = []
MAXCount = 3000
for n in range(40):
  lowCount = 1
  highCount = 1
  while GPIO.input(PIN) == GPIO.LOW:
    lowCount += 1
  while GPIO.input(PIN) == GPIO.HIGH:
    highCount += 1
    if highCount > MAXCount:
      print("missing data")
      exit(1)
  if lowCount < highCount:
    bits.append(1)
  else:
    bits.append(0)

RH = 0
RHD = 0
T = 0
TD = 0
checksum = 0
for bit in bits[:8]:
  RH = (RH << 1) | bit
for bit in bits[8:16]:
  RHD = (RHD << 1) | bit
for bit in bits[16:24]:
  T = (T << 1) | bit
for bit in bits[24:32]:
  TD = (TD << 1) | bit
for bit in bits[32:40]:
  checksum = (checksum << 1) | bit
if RH+RHD+T+TD != checksum:
  print("checksum error")
  exit(1)
print("RH: {}%, T: {}C".format(RH+0.1*RHD, T+0.1*TD))
