# iot-pi

A collection of IoT scripts and programs that can be used with the Raspberry Pi

<h2>onOFF.py</h2>
--------
A simple script that lets the user turn his LED on and off by using console commands. Can be reconfigured easily to suit the users setup. By default, it is configured to pin 4. (<a href="http://www.elektronik-kompendium.de/sites/raspberry-pi/fotos/raspberry-pi-15.jpg">Raspberry Pi GPIO pin layout</a>)

<b>Quick Summary:</b>
1. Imports GPIO library
2. Uses the BCM numbering scheme
3. Sets a pin as output
4. Creates a loop
5. Displays user input commands that can be used
6. Loops until the user quits the loop
7. Cleans everything up so that no warnings will be displayed when the script is run again

