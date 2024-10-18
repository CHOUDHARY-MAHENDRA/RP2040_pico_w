from machine import Pin
import time

# Function to create a 10-second delay using busy-waiting
def delay_10s():
    # Record the start time in seconds
    start_time = time.time()  # Use time.ticks() for better precision if needed
    while (time.time() - start_time) < 0.01:  # Wait for 10 seconds
        pass  # Do nothing, just wait

# Setup pin 15 (or any other pin you wish to use) as an output pin
led = Pin("LED", Pin.OUT)

# Main loop
while True:
    led.value(1)  # Set pin high (LED on)
    #time.sleep_us(100000)
    delay_10s()   # Delay for 10 seconds
    led.value(0)  # Set pin low (LED off)
    #time.sleep_us(100000)

    delay_10s()   # Delay for another 10 seconds
