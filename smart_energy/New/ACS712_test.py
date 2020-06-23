import RPi.GPIO as GPIO 
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306, Adafruit_ADS1x15, time
adc = Adafruit_ADS1x15.ADS1115()
#values = adc.read_adc(0, gain=GAIN)
#mcp = adc.read_adc(0, gain=1)

#Initiate variables
sensitivity = 0.2 #ACS712 30A
voltagePerUnit = 5/1023
vcc = 5/2 #Should be 5/2 or 1023/2?

while True:
    data = adc.read_adc(0, gain=1)
    print('Data direct from channel 0:',data) # Pure data from channel 0
    converted = ((data - vcc) * (voltagePerUnit / sensitivity))
    print('Data converted:'+"{:.2f}".format(converted))
    # Pause for half a second.
    time.sleep(2)
