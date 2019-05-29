import RPi.GPIO as GPIO
import time

PIN = 4

class DHT11():
  def __init__(self, pin):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    self._pin = pin

  def _startSignal(self):
    GPIO.setup(self._pin, GPIO.OUT)
    GPIO.output(self._pin, GPIO.LOW)
    time.sleep(0.0181)
    GPIO.output(self._pin, GPIO.HIGH)
    GPIO.setup(self._pin, GPIO.IN, GPIO.PUD_UP)

  def _collectInput(self):
    unchangedCount = 0
    maxUnchangedCount = 500
    last = -1
    inputs = []
    while True:
      current = GPIO.input(PIN)
      inputs.append(current)
      if last != current:
        unchangedCount = 0
        last = current
      else:
        unchangedCount += 1
        if unchangedCount > maxUnchangedCount:
          break
    return inputs

  def _voltagePeriodCount(self, voltageData):
    stateSwitcher = {
      "UnInit": lambda x: "Init",
      "Init": lambda x: "Reading" if x==GPIO.LOW else "Init", 
      "Reading": lambda x: "Reading"
    }

    state = "UnInit"
    current_length = 0
    pre = GPIO.HIGH
    lengths = []
    for x in voltageData:
      if x != pre:
        state = stateSwitcher[state](x)
        lengths.append(current_length)
        current_length = 1
      else:
        current_length += 1
      pre = x
    return lengths[3:-1]

  def _calculateBits(self, voltagePeriod):
    bits = []
    for lowPeriod, highPeriod in zip(voltagePeriod[0::2], voltagePeriod[1::2]):
      bits.append(lowPeriod<highPeriod)
    return bits

  def _bits2Bytes(self, bits):
    bytes = []
    for i in range(0, 40, 8):
      bitsArray = bits[i:i+8]
      byte = 0
      for bit in bitsArray:
        byte = (byte << 1) | bit
      bytes.append(byte)
    return bytes

  def _checkSum(self, bytes):
    return bytes[0]+bytes[1]+bytes[2]+bytes[3]

  def _readImp(self):
    self._startSignal()
    voltageData = self._collectInput()
    #print(voltageData)

    voltagePeriod = self._voltagePeriodCount(voltageData)
    #print(voltagePeriod)
    if len(voltagePeriod) != 80:
       raise Exception("missing data")

    bits = self._calculateBits(voltagePeriod)
    #print(bits)
    bytes = self._bits2Bytes(bits)
    #print(bytes)

    if bytes[4] != self._checkSum(bytes):
      raise Exception("checksum error")
    return (bytes[0]+0.1*bytes[1], bytes[2]+0.1*bytes[3])

  def readOnce(self):
    try:
      return self._readImp()
    except Exception, e:
      print(e)
    return (None, None)

  def read(self):
    testRun = 0
    while testRun < 5:
      try:
        return self._readImp()
      except:
        testRun += 1
        time.sleep(1)
    return (None, None)


if __name__ == "__main__":
  dht11 = DHT11(4) 
  h, t = dht11.read()
  print("RH: {}%, Temperature: {}C".format(h, t))
