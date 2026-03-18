from machine import Pin
import time
import _thread

lock = _thread.allocate_lock()

BUTTON_SCALE_DIVIDERS =[0, 4, 2, 1] # off,  (vibration intensity) * 1/4, ... * 1/2, ... * 1
BUTTON = Pin(15, Pin.IN, Pin.PULL_UP)

div_scale = 1
state = 0
last_button = 1

def button_thread():
    global state, last_button, div_scale
    while True:
        current_button = BUTTON.value()
        if last_button == 1 and current_button == 0:
            with lock:
                state = (state + 1) % len(BUTTON_SCALE_DIVIDERS)
                div_scale = BUTTON_SCALE_DIVIDERS[state]
            time.sleep(0.2)
        last_button = current_button
        time.sleep(0.1)
