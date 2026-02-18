from machine import Pin, PWM

PWM_MAX = 32767
PWM_MIN = 1

MOTORS = {
  "left" : PWM(Pin(6), freq=50, duty_u16=0),
  "right" : PWM(Pin(7), freq=50, duty_u16=0),
}
