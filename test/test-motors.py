from machine import Pin, PWM

PWM_MAX = 200
PWM_MIN = 0

MOTORS = {
  "left" : PWM(Pin(6), freq=128),
}

while True:
  pass

