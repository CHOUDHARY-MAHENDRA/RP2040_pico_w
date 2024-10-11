import network
import socket
from machine import Pin
import time

# Set up the LED (connected to GPIO 15)
led = Pin("LED", Pin.OUT )

# Wi-Fi credentials
 
ssid = '.......'    # enter your ssid 
password = '......'  # enter password


# Connect to Wi-Fi 
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            time.sleep(1)
    print('Network connected:', wlan.ifconfig())

# Start the Wi-Fi connection
connect_wifi(SSID, PASSWORD)

# HTML to serve
html = """<!DOCTYPE html>
<html>
<head><title>Pico W LED Control</title></head>
<body>
<h1>LED Control</h1>
<p>Click the buttons to control the LED.</p>
<button onclick="window.location.href='/on'">Turn ON</button>
<button onclick="window.location.href='/off'">Turn OFF</button>
</body>
</html>
"""

# Start the web server
def web_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Listening on', addr)
    
    while True:
        cl, addr = s.accept()
        print('Client connected from', addr)
        request = cl.recv(1024)
        request = str(request)
        print('Request:', request)
        
        # Parse the request to control the LED
        if '/on' in request:
            led.on()
        elif '/off' in request:
            led.off()
        
        # Send the response (web page)
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(html)
        cl.close()

# Run the web server
web_server()
