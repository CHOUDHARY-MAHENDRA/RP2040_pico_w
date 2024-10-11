import machine
import time

# Callback function to handle GPIO interrupts
def gpio_callback(pin):
    print("Interrupt triggered on GPIO", pin)

# Configure the GPIO pin (e.g., GPIO 15 for input)
BUTTON_PIN = 15
button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

# Attach the interrupt to the GPIO pin
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=gpio_callback)

# Infinite loop
while True:
    time.sleep(0.1)  # Sleep to prevent busy-waiting
