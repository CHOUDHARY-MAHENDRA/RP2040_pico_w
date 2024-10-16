import network
#import socket
import time
import ujson
import urequests

# Replace with your own credentials
 
#SSID = 'ECB_TQIP'    # enter your ssid 
#PASSWORD = ''  # enter password
SSID= "DESKTOP-BNCF5UR 5862"
PASSWORD = "123456789"

#FIREBASE_URL = 'https://database-krashak-default-rtdb.firebaseio.com/soil_samples/'   # p  # adderess of realtime database where store data
FIREBASE_URL = "https://fir-e81d4-default-rtdb.firebaseio.com/"   #m

#API_KEY = 'AIzaSyAhlS6xuYbHeUu4cQ116sGeuIJvG1CYKJQ' # p # api key
API_KEY ="AIzaSyCkbnwQwA8Ly6yGW-kxBxNzoH7lxQLzWb4"  # m

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
   
    ID = int(input("Enter id    : "))
    name = input("Enter name    : ")
    phone = input("Enter phone    : ")
    ph = int(input("Enter phosphorus    : "))
       # Example data 
    data =    {
        "id": ID,
        "name": name,
        "phone": phone,
        "phosphorus": ph
    }

    

    # Example data to send
    #data_to_send = {'temperature': 2, 'humidity': 60}
    send_data(f'{i}', data)
    
    # Retrieve the data back
    get_data(f'{i}')
    print(f"soil_samples{i}")
    
connect_wifi()
i=1
# Run the main function
#while TRUE:
main(i)