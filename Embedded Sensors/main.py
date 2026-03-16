from sensors import *
from util import *
from motors import *
from button import *
from threading import Thread
import time

SLEEP_S = 0.3
DEBUG = True

prev_dist = {
    "left": PWM_MIN,
    "right": PWM_MIN,
    "middle": PWM_MIN,
}

# reads sensor distance
def read_dist(dir):
    current = DIST_SENSORS[dir].distance_mm()
    previous = prev_dist[dir]
    # filters out large spikes in distance readings
    if abs(current - previous) > DIST_MAX_MM:
        return previous
    prev_dist[dir] = current
    return current

# scales from distance to pwm
def scale_distance(dist):
    if dist <= PWM_MIN:
        return PWM_MIN
    scaled = map_range(dist, DIST_MIN_MM, DIST_MAX_MM, PWM_MIN, PWM_MAX)
    return PWM_MAX - scaled

t = Thread(target=button_thread, args=(), daemon=True)
t.start() 

while True:

    for dir in ["left", "right", "middle"]:
        dist = read_dist(dir)
        scaled = scale_distance(dist)
        scaled = scaled // div_scale
        MOTORS[dir].duty_u16(scaled)     

        if DEBUG:
            print(f"{dir}_dist: {dist}")
            print(f"{dir}_dist_scaled: {scaled}\n")

    time.sleep(SLEEP_S)
    