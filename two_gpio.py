import RPi.GPIO as GPIO
import time

# Pin Definitions
GPIO.setmode(GPIO.BCM)

output_pin1 = 17  # BOARD pin 12, BCM pin 18

output_pin2 = 27  # BOARD pin 12, BCM pin 18

#GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)

def epm(input):
	
	if(input == False):

		try:
		
			curr_value1 = GPIO.HIGH
			curr_value2 = GPIO.LOW
			
			GPIO.setmode(GPIO.BCM)
			
			GPIO.setup(output_pin1, GPIO.OUT)
			GPIO.setup(output_pin2, GPIO.OUT)
			
			GPIO.output(output_pin1, curr_value1)
			GPIO.output(output_pin2, curr_value2)
			
			print("Hi Master..!! EPM_PIN (17 - 1, 27 - 0) is Low Now ")
			
		except Exception as e:
		
			print('exception at high_epm',e)

	elif(input == True):

		try:
			curr_value1 = GPIO.LOW
			curr_value2 = GPIO.HIGH
			
			GPIO.setmode(GPIO.BCM)
			
			GPIO.setup(output_pin1, GPIO.OUT)
			GPIO.setup(output_pin2, GPIO.OUT)
			
			GPIO.output(output_pin1, curr_value1)
			GPIO.output(output_pin2, curr_value2)
			
			print("Hi Master..!! EPM_PIN (17 - 0, 27 - 1) is High Now ")
			
		except Exception as e:
		
			print('exception at low_epm',e)
			
	elif(input == 'NTL'):
	
		try:
			curr_value1 = GPIO.LOW
			curr_value2 = GPIO.LOW
			
			GPIO.setmode(GPIO.BCM)
			
			GPIO.setup(output_pin1, GPIO.OUT)
			GPIO.setup(output_pin2, GPIO.OUT)
			
			GPIO.output(output_pin1, curr_value1)
			GPIO.output(output_pin2, curr_value2)
			
			print("Hi Master..!! EPM_PIN (17 - 0, 27 - 0) is NTL ")
			
		except Exception as e:
		
			print('exception at low_epm',e)
			
			
			
			
def gpio_clean():

	print('gpio-cleaned')
	
	GPIO.cleanup()			
