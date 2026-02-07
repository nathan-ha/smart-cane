from hcsr04 import HCSR04

ECHO_TIMEOUT_US = 30000
DIST_MAX_MM = 4000
DIST_MIN_MM = 20 

DIST_SENSORS = {
  "left" : HCSR04(trigger_pin=0, echo_pin=1, echo_timeout_us=ECHO_TIMEOUT_US),
  "right" : HCSR04(trigger_pin=2, echo_pin=3, echo_timeout_us=ECHO_TIMEOUT_US),
  "middle" : HCSR04(trigger_pin=4, echo_pin=5, echo_timeout_us=ECHO_TIMEOUT_US),
}

