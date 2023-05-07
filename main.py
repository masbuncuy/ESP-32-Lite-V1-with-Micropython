import machine
import time

led_g = machine.Pin(17, machine.Pin.OUT)
led_y = machine.Pin(16, machine.Pin.OUT)
led_b = machine.Pin(27, machine.Pin.OUT)
led_r = machine.Pin(19, machine.Pin.OUT)
led_r2 = machine.Pin(5, machine.Pin.OUT)
led_y2 = machine.Pin(18, machine.Pin.OUT)
led_g2 = machine.Pin(23, machine.Pin.OUT)
while True:
    led_r.value(1)
    # time.sleep(1)
    # led_g.value(0)

    led_g.value(1)
    # time.sleep(1)
    # led_g.value(0)

    led_y.value(1)
    # time.sleep(1)
    # led_y.value(0)

    led_b.value(1)
    # time.sleep(1)
    # led_b.value(0)

    led_r2.value(1)
    # time.sleep(1)
    # led_r2.value(0)

    led_y2.value(1)
    # time.sleep(1)
    # led_y2.value(0)

    led_g2.value(1)
    # time.sleep(1)
    # led_g2.value(0)

