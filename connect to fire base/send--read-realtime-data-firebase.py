import network
import socket
import time
import ujson
import urequests

# Replace with your own credentials
ssid = '.......'    # enter your ssid 
password = '......'  # enter password


FIREBASE_URL = 'https://.....'   # adderess of realtime database where store data

API_KEY = ''  # api key
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
def main():
   
    total_sqr_fit = int(input("Enter Total sqre feet    : "))
    bath =int( input("Enter bath    : "))
    bhk = int(input("Enter bhk    : "))
    # Example data 
    data = { 
        "Total_sqr_fit": total_sqr_fit,
        "bath": bath,
        "bhk": bhk
    }   
    
    # Example data to send
    #data_to_send = {'temperature': 2, 'humidity': 60}
    send_data('sensors', data)
     
    # Retrieve the data back
    get_data('sensors')
    print(f"sensor")
    
connect_wifi()
# Run the main function
while True:
    main()   