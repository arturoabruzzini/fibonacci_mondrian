import time
import math
import machine
import network
import ntptime
from interstate75 import *

from draw_utils import *
from time_utils import *
from fibonacci import *
from borders import *

i75 = Interstate75(display=DISPLAY_INTERSTATE75_128X32)
graphics = i75.display

width = i75.width
height = i75.height

set_draw_utils(graphics)

last_second = None


def draw_everything(hour, minute, second, offset_x, offset_y, invert=False):
    draw_borders(graphics, second, offset_x, offset_y, invert)
    # draw_fibonacci(graphics, minute % 35, second, offset_x, offset_y, invert)
    draw_fibonacci(graphics, hour, minute, offset_x, offset_y, invert)


def redraw_display(hour, minute, second):
    clock = "{:02}:{:02}:{:02}".format(hour, minute, second)

    offset_x = 4
    offset_y = 4

    draw_everything(hour, minute, second, offset_x -
                    32, offset_y+32, invert=True)
    draw_everything(hour, minute, second, offset_x+64, offset_y-32)

    # calculate text position so that it is centred
    # w = graphics.measure_text(clock, 1)
    # x = int(width / 2 - w / 2 + 1)
    # y = 11
    # draw_text(graphics, clock, x, y)
    # draw_rect(graphics, 0, 0, 10, 'red')
    # draw_rect(graphics, 0, 22, 10, 'yellow')
    # draw_rect(graphics, 22, 0, 10, 'white')
    # draw_rect(graphics, 22, 22, 10, 'blue')


draw_wait_text(graphics)
i75.update()
# sync_time()

switch_a_pressed = False
switch_b_pressed = False

animate = False
mock_time = 0

while True:

    hour, minute, second = get_time()

    if animate:
        clear_drawing(graphics)
        redraw_display(mock_time, mock_time, mock_time)
        mock_time = mock_time + 1 if mock_time < 59 else 0
        time.sleep(0.1)
    else:
        if second != last_second:
            clear_drawing(graphics)
            redraw_display(hour, minute, second)

    # Update the display
    i75.update()
    last_second = second

    if i75.switch_pressed(SWITCH_A):
        if not switch_a_pressed:
            set_brightness(graphics, -10)
        switch_a_pressed = True
    else:
        switch_a_pressed = False

    if i75.switch_pressed(SWITCH_B):
        if not switch_b_pressed:
            set_brightness(graphics, 10)
        switch_b_pressed = True
    else:
        switch_b_pressed = False
