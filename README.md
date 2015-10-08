# iot-pi

A small collection of IoT scripts that can be used with the Raspberry Pi. See below for more information.

<h2>onOFF.py</h2>
<p>A simple script that lets the user turn his LED on and off by using console commands. Can be reconfigured easily to suit the users setup. By default, it is configured to <b>pin 4</b>. (<a href="http://www.elektronik-kompendium.de/sites/raspberry-pi/fotos/raspberry-pi-15.jpg">Raspberry Pi GPIO pin layout</a>)</p>
<b>Quick Summary:</b><br>
1. Imports GPIO library<br>
2. Uses the BCM numbering scheme<br>
3. Sets a pin as output<br>
4. Creates a loop<br>
5. Displays user input commands that can be used to turn the LED on and off<br>
6. Loops until the user quits the loop<br>
7. Cleans everything up so that no warnings will be displayed when the script is run again<br>
<h2>onOFFweb.py</h2>
Uses the code from onOff.py, but is reworked to be used with Lighttpd web server and the Flup library.
The index.html uses prototype.js library to handle AJAX requests. And has three buttons that correspond to the same commands as used in onOFF.py script.
<br>
To tell the web server where to find the onOFFweb python script, you need to edit <code>/etc/lighttpd/lighttpd.conf</code> Add <code>"mod_fastcgi"</code> to the server.modules list and the following block in the very end. Restart the web server after this.
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
