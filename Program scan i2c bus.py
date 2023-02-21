##Program scan i2c bus 
import machine
sda=machine.Pin(8)
scl=machine.Pin(9)
i2c=machine.I2C(0,sda=sda, scl=scl, req=400000)

print('Scan i2c bus ...')
device = i2c.scan()

if len(device) ==0:
    print("No i2c device !")
else:
    print("i2c device found:"),len(device))
    
    for device in device:
        print("Decimal address: ",device," | Hexa address: ",hex(device)
              