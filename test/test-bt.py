import bluetooth
from ble_simple_peripheral import BLESimplePeripheral
import machine
import time

# Setup BLE
ble = bluetooth.BLE()
p = BLESimplePeripheral(ble)

print("Bluetooth device active, waiting for connection...")

while True:
    if p.is_connected():
        print("Sending Hello World!")
        p.send("Hello World\n")
        time.sleep(2)
