from sensors import *
from util import *
from motors import *
import time

SLEEP_S = 0.3
DEBUG = False

while True:
    # get distance
    left_dist = DIST_SENSORS["left"].distance_mm()
    right_dist = DIST_SENSORS["right"].distance_mm()
    middle_dist = DIST_SENSORS["middle"].distance_mm()
    
    # map distances to pwm values
    left_dist_scaled = map_range(left_dist, DIST_MIN_MM, DIST_MAX_MM, PWM_MIN, PWM_MAX)
    right_dist_scaled = map_range(right_dist, DIST_MIN_MM, DIST_MAX_MM, PWM_MIN, PWM_MAX)
    middle_dist_scaled = map_range(middle_dist, DIST_MIN_MM, DIST_MAX_MM, PWM_MIN, PWM_MAX)
        
    # update vibration speed
    MOTORS["left"].duty_u16(left_dist_scaled)
    MOTORS["right"].duty_u16(right_dist_scaled)
    MOTORS["middle"].duty_u16(middle_dist_scaled)

    if DEBUG:
        print(f"left_dist {left_dist}")
        print(f"right_dist {right_dist}")
        print(f"middle_dist {middle_dist}")
        print(f"left_dist_scaled {left_dist_scaled}")
        print(f"right_dist_scaled {right_dist_scaled}")
        print(f"middle_dist_scaled {middle_dist_scaled}")

    time.sleep(SLEEP_S)
    