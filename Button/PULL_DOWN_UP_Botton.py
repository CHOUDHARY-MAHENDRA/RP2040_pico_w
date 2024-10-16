from machine import Pin

# Pin(pin_no, Pin_mode, [optional args])
# Pin_mode = { Pin.IN ,  Pin.OUT }
#      {  Pin.PULL_DOWN:  A internal pull-down resistor is connected between the pin and ground, ensuring the pin is in a defined state (low or 0) when not being actively driven.  ,
#         Pin.PULL_UP: , a internal pull-up resistor would connect the pin to a high state (3.3V or 1)      }

button_D= Pin(21, Pin.IN, Pin.PULL_DOWN)   # set pin  for PULL_DOWN  
button_U = Pin(21, Pin.IN, Pin.PULL_UP)   # set pin  for PULL_UP  



while True:
    while True:
        if(button_D.value()==1):
            print("button pressed ")
            break
    while True:
    
        if(button_U.value()==0):
            print("button pressed ")
            break
  
    