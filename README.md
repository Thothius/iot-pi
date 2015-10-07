# iot-pi

A collection of IoT scripts and programs that can be used with the Raspberry Pi. See below for documentation and instructions on how and what to use them for. Cheers!

<h2>onOFF.py</h2>

A simple script that lets the user turn his LED on and off by using console commands. Can be reconfigured easily to suit the users setup. By default, it is configured to pin 4. (<a href="http://www.elektronik-kompendium.de/sites/raspberry-pi/fotos/raspberry-pi-15.jpg">Raspberry Pi GPIO pin layout</a>)

<b>Quick Summary:</b><br>
1. Imports GPIO library<br>
2. Uses the BCM numbering scheme<br>
3. Sets a pin as output<br>
4. Creates a loop<br>
5. Displays user input commands that can be used to turn the LED on and off<br>
6. Loops until the user quits the loop<br>
7. Cleans everything up so that no warnings will be displayed when the script is run again


<h2>onOFFweb.py</h2>
Uses the code from onOff.py, but is reworked to be used with Lighttpd web server and the Flup library.

To tell the web server where to find the onOFFweb python script, you need to edit /etc/lighttpd/lighttpd.conf. Add "mod_fastcgi" to the server.modules list and the following block @ the end of the file whole.
<code>
<br>
 fastcgi.server = (<br>
   ".py" => (<br>
     "python-fcgi" => (<br>
       "socket" => "/tmp/fastcgi.python.socket",<br>
       "bin-path" => "/var/www/doStuff.py",<br>
       "check-local" => "disable",<br>
       "max-procs" => 1)<br>
    )<br>
 )<br>
<code/>

