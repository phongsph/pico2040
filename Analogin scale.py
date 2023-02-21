import machine
import time
import math
B = 4275;
R0 = 100000;
potentiometer = machine.ADC(27) #ตั้งค่าเพื่อใช้งาน Pin 27 เป็น Analog input

def convert(x, in_min, in_max, out_min, out_max): #ฟังชั่นสำหรับเทียบบัญญัติไตรยางค์
    return (x - in_min) * (out_max - out_ min) // (in_max - in_min)+ out_min

while True:
    tb = convert(potentiometer.read_u16(),0,65535,0,1023)#เรียกใช้งานฟังชั่นเทียบบัญญัติไตรยางค์
    
    R = ((1023.0/tb)-1.0)*R0  #แปลงค่า Analog Input ที่อ่านได้ไปเป็น Temp
    temp = (1.0/(math.log(R/100000)/B+1/298.15))-273.15
    print("%2f" % temp)
    time.sleep(2)
    