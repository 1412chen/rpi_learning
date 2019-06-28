import RPi.GPIO as GPIO
import time

#ROW
PIN1 = 2
PIN2 = 3
PIN3 = 4
PIN4 = 17
#COL
PIN5 = 27
PIN6 = 22
PIN7 = 10
PIN8 = 9

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(PIN1, GPIO.IN)
GPIO.setup(PIN2, GPIO.IN)
GPIO.setup(PIN3, GPIO.IN)
GPIO.setup(PIN4, GPIO.IN)
GPIO.setup(PIN5, GPIO.OUT)
GPIO.setup(PIN6, GPIO.OUT)
GPIO.setup(PIN7, GPIO.OUT)
GPIO.setup(PIN8, GPIO.OUT)
GPIO.output(PIN5, GPIO.HIGH)
GPIO.output(PIN6, GPIO.HIGH)
GPIO.output(PIN7, GPIO.HIGH)
GPIO.output(PIN8, GPIO.HIGH)

def callback(RowPin):
  for testColPin in [PIN5, PIN6, PIN7, PIN8]:
    GPIO.output(testColPin, GPIO.LOW)
    if GPIO.input(RowPin) == GPIO.LOW:
      ColPin = testColPin
      break
  print("{}, {}".format(RowPin, ColPin))
  value = {PIN1: {PIN5: '1', PIN6: '2', PIN7: '3', PIN8: 'A'},
           PIN2: {PIN5: '4', PIN6: '5', PIN7: '6', PIN8: 'B'},
           PIN3: {PIN5: '7', PIN6: '8', PIN7: '9', PIN8: 'C'},
           PIN4: {PIN5: '*', PIN6: '0', PIN7: '#', PIN8: 'D'}}[RowPin][ColPin]
  print(value)
  GPIO.output(PIN5, GPIO.HIGH)
  GPIO.output(PIN6, GPIO.HIGH)
  GPIO.output(PIN7, GPIO.HIGH)
  GPIO.output(PIN8, GPIO.HIGH)

GPIO.add_event_detect(PIN1, GPIO.RISING, bouncetime=200, callback=callback)
GPIO.add_event_detect(PIN2, GPIO.RISING, bouncetime=200, callback=callback)
GPIO.add_event_detect(PIN3, GPIO.RISING, bouncetime=200, callback=callback)
GPIO.add_event_detect(PIN4, GPIO.RISING, bouncetime=200, callback=callback)

while True:
  time.sleep(10)
