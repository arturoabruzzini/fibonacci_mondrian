import math
import machine
from interstate75 import Interstate75, DISPLAY_INTERSTATE75_32X32
from time_utils import get_time, sync_time
from draw_utils import draw_text

i75 = Interstate75(display=DISPLAY_INTERSTATE75_32X32)
graphics = i75.display

year, month, day, wd, hour, minute, second = get_time()

last_second = second

# Check whether the RTC time has changed and if so redraw the display


def redraw_display_if_reqd():
    global year, month, day, wd, hour, minute, second, last_second
    year, month, day, wd, hour, minute, second = get_time()
    if second != last_second:
        clock = "{:02}:{:02}:{:02}".format(hour, minute, second)

        # calculate text position so that it is centred
        w = graphics.measure_text(clock, 1)
        x = int(width / 2 - w / 2 + 1)
        y = 11

        draw_text(clock, x, y)

        last_second = second


sync_time()

while True:

    redraw_display_if_reqd()

    # Update the display
    i75.update()
