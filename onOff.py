#!/usr/bin/python

# A simple ON/OFF LED script to run in a console. Right now I have connected my LED to pin 4.


import RPi.GPIO as IO		# References the GPIO library and sets it as IO
import time					# Import 'time' library. Allows the script to use 'sleep'
number = 3					# How many times the LED blinks
speed = 1					# How fast the LED blinks

IO.setmode(IO.BCM)			# Uses the BCM numbering scheme for this bus
IO.setup(4, IO.OUT)			# Sets up pin 4 as output

while(True):		# Keeps on looping until we quit the loop
	key = raw_input("q=ON | w=OFF | e=QUIT | a=Blink 3x | ENTER to execute command: ") # Information for the user / console input

	if key =="q":		# If 'q' is pressed, turns ON the LED@pin4
		IO.output(4,True)

	elif key == "w": 	# If 'w' is pressed, turns OFF the LED@pin4
		IO.output(4,False)
		
	elif key =="a":		# If 'a' is pressed, blinks LED@pin4 three times 
	
		Blink3(int(number),float(speed))	

	elif key == "e":		# If 'e' is pressed, quits the loop and program
		break
	else:
		break			# Even if 'e' is not pressed, quits the program anyway

IO.cleanup		# Used so that no warnings will be generated the next time the program is run



def Blink3(number,speed):
	for i in range(0,number):		#Runs loop 3 times
		IO.output(4,True)
		time.sleep(1)
		IO.output(4,True)
		time.sleep(1)
		IO.output(4,True)
		time.sleep(1)
		print"Done blinking"		#Prints "Done" when complete
		IO.cleanup()

