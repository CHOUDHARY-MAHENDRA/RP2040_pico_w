from machine import Pin, PWM
from time import sleep

analog= PWM(Pin(0))

analog.freq(1000)
analog.duty_u16(0)

while True:
    pwm= float(input("enter voltage "))
    volt=(65550/3.3)*pwm
    analog.duty_u16(int(volt))