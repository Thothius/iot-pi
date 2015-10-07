# iot-pi

A collection of IoT scripts and programs that can be used with the Raspberry Pi. See below for documentation and instructions on how and what to use them for. Cheers!

<h2>onOFF.py</h2>

<p>A simple script that lets the user turn his LED on and off by using console commands. Can be reconfigured easily to suit the users setup. By default, it is configured to pin 4. (<a href="http://www.elektronik-kompendium.de/sites/raspberry-pi/fotos/raspberry-pi-15.jpg">Raspberry Pi GPIO pin layout</a>)</p>

<b>Quick Summary:</b><br>
1. Imports GPIO library<br>
2. Uses the BCM numbering scheme<br>
3. Sets a pin as output<br>
4. Creates a loop<br>
5. Displays user input commands that can be used to turn the LED on and off<br>
6. Loops until the user quits the loop<br>
7. Cleans everything up so that no warnings will be displayed when the script is run again<br>


<h2>onOFFweb.py</h2>
<p>Uses the code from onOff.py, but is reworked to be used with Lighttpd web server and the Flup library.
The index.html uses prototype.js library to handle AJAX requests. And has three buttons that correspond to the same commands as used in onOFF.py script. <b>To tell the web server where to find the onOFFweb python script, you need to edit /etc/lighttpd/lighttpd.conf. Add "mod_fastcgi" to the server.modules list and the following block @ the very end.</b></p>

<code>
<pre>
 fastcgi.server = (
   ".py" => (
     "python-fcgi" => (
       "socket" => "/tmp/fastcgi.python.socket",
       "bin-path" => "/var/www/doStuff.py",
       "check-local" => "disable",
       "max-procs" => 1)
    )
 )
 </pre>
<code/>


