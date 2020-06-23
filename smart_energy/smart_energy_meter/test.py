import time
from noval_twofish import encrypt_data
from firebase import firebase
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306, Adafruit_ADS1x15, time
from PIL import Image, ImageDraw, ImageFont


# COnstants for ADC sensor
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

# 128x64 display with hardware I2C:
display = Adafruit_SSD1306.SSD1306_128_64(rst=None)
# Setup for display
display.begin()  # initialize graphics library for selected display module
display.clear()  # clear display buffer
display.display()  # write display buffer to physical display
displayWidth = display.width  # get width of display
displayHeight = display.height  # get height of display
image = Image.new('1', (displayWidth, displayHeight))  # create graphics library image buffer
draw = ImageDraw.Draw(image)  # create drawing object
font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 30)

data = 0
start_time = time.time()
power = 0.012
while True:

	# Collecting and calculating the information of power.
	for i in range (5):
		in_data = adc.read_adc(0, gain=GAIN)
		data += in_data
	data = data/5
	power+=(0.012*5)
	time_now= (time.time() - start_time)
	if data >= 20225:
		amps = 0.0001
	elif data >= 20370:
		amps = 0.35
	elif data >= 20450:
		amps = 0.5
	else:
		amps = 0.30
		pass
	powr = "{:.2f} W".format(power)
	print("Power: ", powr)
	encrypted_power= encrypt_data(powr)
	print("Encrypted Power:", encrypted_power)
	# Posting the data to Firebase database.
	firebas = firebase.FirebaseApplication('https://smart-energy-meter-ed634.firebaseio.com/')
	result = firebas.post('smart-energy-meter-ed634', {'power': str(powr),'enc_power': str(encrypted_power)})

	# Displaying the info on OLED display
	draw.rectangle((0,0,displayWidth,displayHeight), outline=0, fill=0)
	#values = adc.read_adc(0, gain=GAIN)
	# Draw text
	draw.text((0,0), "Power\n{:.2f}".format(power), font=font, fill=255)
	#draw.text((0,0), '{0:>6}'.format(values), font=font, fill=255)  # print text to image buffer
	# Display to screen
	display.image(image)  # set display buffer with image buffer
	display.display()  # write display buffer to physical display
	display.clear()  # clear display buffer
	data = 0
	time.sleep(5)

# Cleanup the OLED screen.
GPIO.cleanup()  # release all GPIO resources
