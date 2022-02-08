import hid
import time
VENDOR_ID = 0x2123
PRODUCT_ID = 0x1010

device = hid.device()
device.open(VENDOR_ID, PRODUCT_ID)

#LED On
device.write(bytearray(b'\x00\x03\x01\x00\x00\x00\x00\x00'))

#Turn Right
device.write(bytearray(b'\x00\x02\x08\x00\x00\x00\x00\x00'))
time.sleep(0.5)
#Stop Turning Right
device.write(bytearray(b'\x00\x02\x20\x00\x00\x00\x00\x00'))
time.sleep(0.5)

#Turn Left
device.write(bytearray(b'\x00\x02\x04\x00\x00\x00\x00\x00'))
time.sleep(0.5)
#Stop Turning Left
device.write(bytearray(b'\x00\x02\x20\x00\x00\x00\x00\x00'))
time.sleep(0.5)

#Turn Up
device.write(bytearray(b'\x00\x02\x02\x00\x00\x00\x00\x00'))
time.sleep(0.75)
#Stop Turning Up
device.write(bytearray(b'\x00\x02\x20\x00\x00\x00\x00\x00'))
time.sleep(0.5)

#Turn Down
device.write(bytearray(b'\x00\x02\x01\x00\x00\x00\x00\x00'))
time.sleep(0.5)
#Stop Turning Down
device.write(bytearray(b'\x00\x02\x20\x00\x00\x00\x00\x00'))
time.sleep(0.5)

#Shoot
device.write(bytearray(b'\x00\x02\x10\x00\x00\x00\x00\x00'))
time.sleep(4)
#Stop Shooting
device.write(bytearray(b'\x00\x02\x20\x00\x00\x00\x00\x00'))
time.sleep(0.5)