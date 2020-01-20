import ssd1306, machine

def start_oled(scl_pin=5, sda_pin=4, w=128, h=32):
    i2c = machine.I2C(scl=machine.Pin(scl_pin), sda=machine.Pin(sda_pin))
    oled = ssd1306.SSD1306_I2C(w, h, i2c)
    oled.fill(0)
    return oled 