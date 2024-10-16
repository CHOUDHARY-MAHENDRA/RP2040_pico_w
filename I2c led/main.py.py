from machine import Pin, SoftI2C

from pico_i2c_lcd import I2cLcd
import utime

sda=Pin(0)
scl=Pin(1)
#i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)
i2c=SoftI2C(sda=sda, scl=scl, freq=400000)
 
print('Scan i2c bus...')
devices = i2c.scan()
 
if len(devices) == 0:
    print("No i2c device !")
else:
  print('i2c devices found:',len(devices))
 
  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))
    
lcd=I2cLcd(i2c,0x3f,2,16)
lcd.putstr("5h")
#lcd.putint(5)



utime.sleep(2)
#i2c.readfrom(0x3f, 4)   # read 4 bytes from device with address 0x3a
# i2c.writeto(0x27, '12')
# write '12' to device with address 0x3a
#i2c.
#buf = bytearray(10)     # create a buffer with 10 bytes
#i2c.writeto(0x27, buf)
      
    