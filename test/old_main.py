from sensors import *
from util import *
from motors import *
import time

SLEEP_S = 0.3


DEBUG = True

prev_left = prev_right = prev_middle = PWM_MIN

while True:
    # get distance
    left_dist = DIST_SENSORS["left"].distance_mm()
    right_dist = DIST_SENSORS["right"].distance_mm()
    middle_dist = DIST_SENSORS["middle"].distance_mm()
    
    # scale distances
    if abs(left_dist - prev_left) > DIST_MAX_MM:
        left_dist= prev_left
    else:
        prev_left = left_dist
    left_dist_scaled = PWM_MAX - map_range(left_dist, DIST_MIN_MM, DIST_MAX_MM, PWM_MIN, PWM_MAX) if left_dist > PWM_MIN else PWM_MIN
    
    
    if abs(right_dist - prev_right) > DIST_MAX_MM:
        right_dist= prev_right
    else:
        prev_right = right_dist
    right_dist_scaled = PWM_MAX - map_range(right_dist, DIST_MIN_MM, DIST_MAX_MM, PWM_MIN, PWM_MAX) if right_dist > PWM_MIN else PWM_MIN
    
    
    if abs(middle_dist - prev_middle) > DIST_MAX_MM:
        middle_dist= prev_middle
    else:
        prev_middle = middle_dist
    middle_dist_scaled = PWM_MAX - map_range(middle_dist, DIST_MIN_MM, DIST_MAX_MM, PWM_MIN, PWM_MAX) if middle_dist > PWM_MIN else PWM_MIN


    
    # update vibration speed
    MOTORS["left"].duty_u16(left_dist_scaled)
    MOTORS["right"].duty_u16(right_dist_scaled)
    MOTORS["middle"].duty_u16(middle_dist_scaled)
    
        

    if DEBUG:
        #print(f"left_dist {left_dist}")
        #print(f"right_dist {right_dist}")
        #print(f"middle_dist {middle_dist}")
        print(f"left_dist_scaled {left_dist_scaled}")
        print(f"right_dist_scaled {right_dist_scaled}")
        print(f"middle_dist_scaled {middle_dist_scaled}")

    time.sleep(SLEEP_S)
    
