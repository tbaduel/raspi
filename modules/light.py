import os
import RPi.GPIO as GPIO

#os.system("gpio write 7 1")
GPIO.setmode(GPIO.BOARD)

def getStatus(pin):
	
	state = GPIO.gpio_function(pin)
	print(state)
	return state	



def lightOn(pin):
	os.system("gpio write %s 1", pin)

def LightOff(pin):
	os.sytem("gpio write %s 0", pin)

status = getStatus(7)
