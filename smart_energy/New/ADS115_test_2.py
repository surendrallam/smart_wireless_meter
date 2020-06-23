# ADS1115 single-shot mode
import i2cdev
import os
from time import sleep

ADS1115 = i2cdev.I2C(0x48,1) # Address = 0x48, I2C bus = 0


def ADS1115_read():
  sleep(0.001)
  ADS1115.write(bytes([int(1),int(245),int(131)])) # write config =1 & chanel 3 + FSE 2v + single shot & 128hz + b00011
  sleep(0.008) # wait for conversion
  ADS1115.write(bytes([int(0)])) # change the pointer to measurment buffer
  sleep(0.001)
  out = int.from_bytes(ADS1115.read(2), byteorder='big')
  return out

ADS=float(ADS1115_read())
const=(2.0/32676)
error=ADS*const

if error >= 0.82:
	n=4
	correct=17.10
elif error >= 0.70:
	n=3
	correct=13.26
else:
	n=1
	correct=1

full=n*4.2
null=n*3.3
diff=n*0.9
	

while True:
	ADS=float(ADS1115_read())
	const=(5.0/32676)
	error=ADS*const
	voltage=correct*error
	volt= float("{0:.2f}".format(error))
	print("ADS: {0:.2f}".format(ADS))
	print("Battery Voltage: {0:.2f}".format(error))
	sleep(2)
