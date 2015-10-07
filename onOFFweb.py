#!/usr/bin/pythonRoot

import RPi.GPIO as IO     
from flup.server.fcgi import WSGIServer 
import sys, urlparse
import time					# Import 'time' library. Allows the script to use 'sleep'

# CONFIGURATION
number = 3					# How many times the LED blinks
speed = 1					# How fast the LED blinks

IO.setmode(IO.BCM)
IO.setup(4, IO.OUT)

def Blink(number,speed):	# Defines the Blink function
	for i in range(0,number):		#Runs loop 3 times
		IO.output(4,True)
		time.sleep(1)
		IO.output(4,False)
		time.sleep(1)

def app(environ, start_response):		# Starts the http response
  start_response("200 OK", [("Content-Type", "text/html")])
  i = urlparse.parse_qs(environ["QUERY_STRING"])		# Looks for inputs on the URL
 
  yield ('&nbsp;') # FLUP expects a string, so lets make one, in this case 'r' as in run
 
  if "r" in i:		# if there's a url variable named 'r'
    if i["r"][0] == "q": 
      IO.output(4, True)   # Turn it on
    elif i["r"][0] == "w":
      IO.output(4, False)  # Turn it off
	elif i["r"][0] == "a":
      Blink(int(number),float(speed))
	 

WSGIServer(app).run()