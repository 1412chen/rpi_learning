import datetime
import pyRPiRTC

rtc = pyRPiRTC.DS1302()
#rtc.write_datetime(datetime.datetime.utcnow())
print(rtc.read_datetime())

