from hcsr04 import HCSR04

ECHO_TIMEOUT_US = (30000)
DIST_MAX_MM = 500
DIST_MIN_MM = 20 

DIST_SENSORS = {
  "left" : HCSR04(trigger_pin=27, echo_pin=26, echo_timeout_us=ECHO_TIMEOUT_US),
  "right" : HCSR04(trigger_pin=22, echo_pin=21, echo_timeout_us=ECHO_TIMEOUT_US),
  "middle" : HCSR04(trigger_pin=20, echo_pin=19, echo_timeout_us=ECHO_TIMEOUT_US),
}
