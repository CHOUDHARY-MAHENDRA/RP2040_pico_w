import network
import urequests
import time
import json

# Replace these with your Firebase URL and Wi-Fi credentials
ssid = '.......'    # enter your ssid 
password = '......'  # enter password


FIREBASE_URL = 'https://.....'   # adderess of realtime database where store data

API_KEY = ''  # api key
# Connect to Wi-Fi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    
    while wlan.isconnected() == False:
        print("Waiting for connection...")
        time.sleep(1)
    
    print("Connected to WiFi:", wlan.ifconfig())

# Send data to Firebase
def send_data_to_firebase(data):
    headers = {"Content-Type": "application/json"}
    response = urequests.post(FIREBASE_URL, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        print("Data sent successfully!")
    else:
        print("Failed to send data:", response.status_code, response.text)
    
    response.close()

# Main loop
def main(): 
    connect_to_wifi()
    total_sqr_fit = input("Enter Total sqre feet    : ")
    bath = input("Enter bath    : ")
    bhk = input("Enter bhk    : ")
    # Example data 
    data = { 
        "Total_sqr_fit": total_sqr_fit,
        "bath": bath,
        "bhk": bhk
    }
    
    # Send the data 
    send_data_to_firebase(data)
    
    # Send data every 10 seconds
    while True:
        send_data_to_firebase(data)
        time.sleep(10)

# Run the main function
main()
