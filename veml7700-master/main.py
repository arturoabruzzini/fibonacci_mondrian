# standard libraries
import time
from interstate75 import *

# this library
import veml7700

# setup i2c bus
i75 = Interstate75(display=DISPLAY_INTERSTATE75_128X32)
i2c = i75.i2c

# setup sensor with intergartion time 100 ms and gain 1/8
veml = veml7700.VEML7700(address=0x10, i2c=i2c, it=100, gain=1/8)

while True:
    # read the ambient light brightness
    lux_val = veml.read_lux()
    print(lux_val)
    time.sleep(1)
