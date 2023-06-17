import time
import math
import machine
import network
import ntptime
from interstate75 import Interstate75, DISPLAY_INTERSTATE75_32X32

from draw_utils import *
from time_utils import *

i75 = Interstate75(display=DISPLAY_INTERSTATE75_32X32)
graphics = i75.display

width = i75.width
height = i75.height

set_draw_utils(graphics)

last_second = None

############
### MAIN ###
############

# Check whether the RTC time has changed and if so redraw the display
def redraw_display(hour, minute, second):
    clock = "{:02}:{:02}:{:02}".format(hour, minute, second)

    # calculate text position so that it is centred
    w = graphics.measure_text(clock, 1)
    x = int(width / 2 - w / 2 + 1)
    y = 11
    draw_text(graphics, clock, x, y)
    draw_rect(graphics, 0, 0, 10, 'red')
    draw_rect(graphics, 0, 22, 10, 'yellow')
    draw_rect(graphics, 22, 0, 10, 'white')
    draw_rect(graphics, 22, 22, 10, 'blue')

draw_wait_text(graphics)
i75.update()
# sync_time()

while True:

    hour, minute, second = get_time()
    if second != last_second:
        clear_drawing(graphics)
        redraw_display(hour, minute, second)

    # Update the display
    i75.update()
    last_second = second
