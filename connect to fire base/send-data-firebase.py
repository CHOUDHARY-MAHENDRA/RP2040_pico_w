import network
import urequests
import time
import json

# Replace these with your Firebase URL and Wi-Fi credentials
FIREBASE_URL = "https://home-automation-35494-default-rtdb.firebaseio.com/DATA/temp.json"  # Add the .json extension for Realtime DB
#WIFI_SSID = "ECB_TEQIP"
#WIFI_PASSWORD = ""
WIFI_SSID ="vivo Y100A";
WIFI_PASSWORD = "zxcvbnm12";
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
    
    # Example data 
    data = { 
        "sensor_value": 25,
        "timestamp": time.time()
    }
    
    # Send the data 
    send_data_to_firebase(data)
    
    # Send data every 10 seconds
    while True:
        send_data_to_firebase(data)
        time.sleep(10)

# Run the main function
main()
