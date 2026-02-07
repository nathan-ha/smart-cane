from machine import Pin, PWM

PWM_MAX = 200
PWM_MIN = 0

MOTORS = {
  "left" : PWM(Pin(6), freq=PWM_MIN),
  "right" : PWM(Pin(7), freq=PWM_MIN),
  "middle" : PWM(Pin(8), freq=PWM_MIN),
}