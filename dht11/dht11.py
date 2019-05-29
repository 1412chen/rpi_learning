import Adafruit_DHT as dht

PIN = 4
SENSOR = dht.DHT11
print( dht.read_retry(SENSOR, PIN) )

