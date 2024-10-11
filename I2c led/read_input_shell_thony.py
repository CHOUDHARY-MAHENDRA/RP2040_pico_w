# MicroPython real-time user input example for Raspberry Pi Pico W

import time

# Infinite loop to keep asking for input
while True:
    # Ask user for input
    user_input = int(input("Enter something: "))

    # Print the user input to the console
    print("You entered:", user_input)

    # Add a short delay to prevent rapid looping
    time.sleep(0.1)
