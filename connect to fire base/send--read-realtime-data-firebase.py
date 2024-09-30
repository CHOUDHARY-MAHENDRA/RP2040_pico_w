import network
import socket
import time
import ujson
import urequests

# Replace with your own credentials
SSID = 'vivo Y100A'
PASSWORD = 'zxcvbnm12'
FIREBASE_URL = 'https://home-automation-35494-default-rtdb.firebaseio.com/DATA/'
API_KEY = 'AIzaSyD1fkL-uYNxfDKa58XQ4UK9us8XGcVBPfM' 

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        time.sleep(1)
    print('Connected to Wi-Fi:', wlan.ifconfig())
    
# Function to send data to Firebase
def send_data(path, data):
    url = f'{FIREBASE_URL}{path}.json?auth={API_KEY}'
    response = urequests.put(url, json=data)
    print('Data sent:', response.text)
    response.close()

# Function to get data from Firebase
def get_data(path):
    url = f'{FIREBASE_URL}{path}.json?auth={API_KEY}'
    response = urequests.get(url)
    if response.status_code == 200:
        data = ujson.loads(response.text)
        print('Data received:', data)
    else:
        print('Error getting data:', response.status_code)
    response.close()

# Main function
def main(i):
   
        
    
    # Example data to send
    data_to_send = {'temperature': 2, 'humidity': 60}
    send_data(f'sensors{i}/data', data_to_send)
    
    # Retrieve the data back
    get_data(f'sensors{i}/data')
    print(f"sensor{i}")
    
connect_wifi()
i=0
# Run the main function
while True:
   
    i=i+1
    main(i)
    
