import time
from firebase import firebase

while True:
#store the Host ID(provided in firebase database) in variable where you want to send the real time sensor data.  
	firebas= firebase.FirebaseApplication('https://smart-energy-meter-ed634.firebaseio.com/')

#store the readings in variable and convert it into string and using firbase.post then data will be posted to databse of firebase 
	result = firebas.post('smart-energy-meter-ed634', {'cTemp':"hello this is for testing"})
	print(result)
	time.sleep(3)
