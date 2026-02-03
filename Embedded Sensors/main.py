from machine import Pin, PWM
from hcsr04 import HCSR04
import time

sensor01 = HCSR04(trigger_pin=0, echo_pin=1, echo_timeout_us=30000)
sensor02 = HCSR04(trigger_pin=2, echo_pin=3, echo_timeout_us=30000)
sensor03 = HCSR04(trigger_pin=4, echo_pin=5, echo_timeout_us=30000)

motor = PWM(Pin(6), freq=50) 
motor.duty_u16(0)

while True:
    try:
        distance_01 = sensor01.distance_mm()
        distance_02 = sensor02.distance_mm()
        distance_03 = sensor03.distance_mm()
        print(f'Distance_01: {distance_01}')
        print(f'Distance_02: {distance_02}')
        print(f'Distance_03: {distance_03}')
    except OSError as e:
        print('Error:', e)
    time.sleep(0.3)
