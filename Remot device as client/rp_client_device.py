import network
import socket
import machine
import time

# Replace with your Wi-Fi credentials


# GPIO for the LED
led_pin = machine.Pin(15, machine.Pin.OUT)  # Change the pin to your choice (GPIO15)


#ssid = 'vivo Y100A'
#password = 'zxcvbnm12'

ssid='ECB_TEQIP'
password=''
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
    #raise RuntimeError('network connection failed')
    print("failed")
else:
#while True: 
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    time.sleep(10)

# Define the web server
def handle_request(client):
    request = client.recv(1024)
    request = str(request)
    print("Request:", request)

    if '/led/on' in request:
        led_pin.value(1)  # Turn LED on
        response = "LED is ON"
    elif '/led/off' in request:
        led_pin.value(0)  # Turn LED off
        response = "LED is OFF"
    else:
        response = "Invalid request"

    # Send HTTP response
    client.send('HTTP/1.1 200 OK\r\n')
    client.send('Content-Type: text/plain\r\n')
    client.send('\r\n')
    client.send(response)
    client.close()
# Create a socket and listen for incoming requests
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('Listening on', addr)
print("Server started, waiting for connections...")

# Main loop to handle requests
while True:
    client, address = s.accept()
    print('Client connected from', address)
    handle_request(client)