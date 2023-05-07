import machine

# led green
led_g = machine.Pin(17, machine.Pin.OUT)
# led yellow
led_y = machine.Pin(16, machine.Pin.OUT)
# led blue
led_b = machine.Pin(27, machine.Pin.OUT)
# led red
led_r = machine.Pin(19, machine.Pin.OUT)

# led traffic

# led red
led_r2 = machine.Pin(5, machine.Pin.OUT)

# led yellow
led_y2 = machine.Pin(18, machine.Pin.OUT)

# led green
led_g2 = machine.Pin(23, machine.Pin.OUT)

# tinggal diulang-ulang panggil pin yang sudah dideklarasikan

while True:
    led_g.value(1)
    led_y.value(1)
    led_b.value(1)
    led_r.value(1)

    led_r2.value(1)
    led_y2.value(1)
    led_g2.value(1)
