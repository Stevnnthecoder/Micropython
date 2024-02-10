from machine import Pin, PWM
import utime 

color1 = PWM(Pin(14))
color1.freq(500)#Hz

color2 = PWM(Pin(15))
color2.freq(500) #Hz

color3 = PWM((Pin(9)))
color3.freq(1000)#Hz

for i in range(100):
    color1.duty_u16(i*655)
    color2.duty_u16((100-i)*655)
    utime.sleep_ms(100)