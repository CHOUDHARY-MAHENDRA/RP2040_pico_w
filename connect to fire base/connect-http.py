
import network
import socket
import time
from machine import Pin
led = Pin("LED", Pin.OUT)

html = """<!DOCTYPE html>
 <html>
     <head> <title>Pico W</title> </head>
     <body> <h1>Pico W</h1>
         <p>%s</p>
     </body>
 </html>
 """
 
ssid = '.......'    # enter your ssid 
password = '......'  # enter password

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

 # Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    
# Open socket
ip = wlan.ifconfig()[0]
addr_info = socket.getaddrinfo(ip, 80)[0]  # Get full info tuple
addr = addr_info[4]  # Extract address for bind()

    # Create a socket and listen on port 80
s = socket.socket()  # Use explicit AF_INET and SOCK_STREAM
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(addr)
s.listen(1)
 
print('listening on', addr)
 
# Listen for connections
def web():    
    cl, addr = s.accept()
    print('client connected from', addr)
    request = cl.recv(1024)
    print(request)
    
    request = str(request)
    led_on = request.find('/light/on')
    led_off = request.find('/light/off')
    print( 'led on = ' + str(led_on))
    print( 'led off = ' + str(led_off))
    
    if led_on == 6:
        print("led on")
        led.value(1)
        stateis = "LED is ON"
    if led_off == 6:
        print("led off")
        led.value(0)
        stateis = "LED is OFF"

    response = html % stateis
 
    cl.send(f'HTTP/1.0 200 OK\r\nContent-type: text/{html}\r\n\r\n')   
    cl.send(response)
    cl.close()
while True:
    
    web()                 