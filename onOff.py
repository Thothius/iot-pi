#!/usr/bin/python

# A simple ON/OFF LED script to run in a console. Right now I have connected my LED to pin 4.


import RPi.GPIO as IO		# References the GPIO library and sets it as IO
IO.setmode(IO.BCM)			# Uses the BCM numbering scheme for this bus
IO.setup(4, IO.OUT)			# Sets up pin 4 as output

while(True):		# Keeps on looping until we quit the loop
	key = raw_input("q=ON | w=OFF | e=QUIT | ENTER to execute command: ") # Information for the user / console input

	if key =="q":		# If 'q' is pressed, turns ON the LED@pin4
		IO.output(4,True)

	elif key == "w": 	# If 'w' is pressed, turns OFF the LED@pin4
		IO.output(4,False)

	elif key == "e":		# If 'e' is pressed, quits the loop and program
		break
	else:
		break			# Even if 'e' is not pressed, quits the program anyway

IO.cleanup		# Used so that no warnings will be generated the next time the program is run

#Added extra line to the end, so no warnings would be present when viewing the file in GitHub
