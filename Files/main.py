from machine import Pin
import utime as time
#from pico_i2c_lcd import I2cLcd
#from machine import I2C
#from dht import DHT11, InvalidChecksum
from dht import DHT11
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd


I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=machine.Pin(4), scl=machine.Pin(5), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
time.sleep(1)

while True:
    time.sleep(3) #this needs to be more than one second in order for it to work properly
    pin = Pin(15, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    sensor.measure()
    #time.sleep(3)
    t  = sensor.temperature
    h = sensor.humidity
    print(t)
    print(h)
    #time.sleep(3)
    lcd.move_to(0,0)
    lcd.putstr("Temp: {}".format(t))
    lcd.move_to(0,1)
    lcd.putstr("Humid: {}".format(h))