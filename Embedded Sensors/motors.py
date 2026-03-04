from machine import Pin, PWM

PWM_MAX = 32767
PWM_MIN = 1

MOTORS = {
  "left" : PWM(Pin(16), freq=50, duty_u16=0),
  "right" : PWM(Pin(17), freq=50, duty_u16=0),
  "middle": PWM(Pin(18)), freq=50, duty_u16=0),
}
