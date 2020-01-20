import esp, time
esp.osdebug(None)

import machine, ssd1306, util

led = machine.Pin(2, machine.Pin.OUT)
led.value(0)


oled = util.start_oled()
oled.text("Starting...", 1,1)
oled.text("...", 1,11)
oled.show()

time.sleep(1)

oled.fill(0)
oled.text("Who's the man?", 10, 10)
oled.pixel(0,0,1)
oled.pixel(127,0,1)
oled.pixel(0,31,1)
oled.pixel(127,31,1)

oled.show()
time.sleep(1)

while True:
    oled.fill(0)
    oled.text("Who's the man?", 10, 10)
    time.sleep(0.5)
    oled.show()
    
    oled.fill(0)
    oled.text("Who's the    ?", 10, 10)
    time.sleep(0.5)
    oled.show()

import gc
gc.collect()
