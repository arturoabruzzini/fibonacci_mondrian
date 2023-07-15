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
import veml7700

i75 = Interstate75(display=DISPLAY_INTERSTATE75_128X32)
graphics = i75.display

width = i75.width
height = i75.height

set_draw_utils(graphics)

last_second = None

veml = veml7700.VEML7700(address=0x10, i2c=i75.i2c, it=100, gain=1/8)


def draw_everything(hour, minute, second, offset_x, offset_y, invert=False):
    draw_borders(graphics, second, offset_x, offset_y, invert)
    draw_rect(graphics, offset_x, 34 + offset_y,
              21, 21, 'white', invert)
    draw_fibonacci(graphics, hour, minute, offset_x, offset_y, invert)


def redraw_display(hour, minute, second):
    clock = "{:02}:{:02}:{:02}".format(hour, minute, second)

    offset_x = 4
    offset_y = 4

    draw_everything(hour, minute, second, offset_x -
                    32, offset_y+32, invert=True)
    draw_everything(hour, minute, second, offset_x+64, offset_y-32)


draw_wait_text(graphics)
i75.update()
# sync_time()

switch_a_pressed = False
switch_b_pressed = False

animate = False
mock_time = 0


def interpolate(input_value, input_min, input_max, output_min, output_max):
    ratio = (input_value - input_min) / (input_max - input_min)
    output_value = ratio * (output_max - output_min) + output_min
    return output_value


def automatic_brightness():
    lux_val = veml.read_lux()
    print('Lux value:', lux_val)
    brightness = set_brightness(
        graphics, interpolate(lux_val, 0, 500, 10, 100))

    draw_text(graphics, str(round(brightness)), 68, 20)
    draw_text(graphics, str(round(lux_val)), 58, 18, True)


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
            automatic_brightness()

    # Update the display
    i75.update()
    last_second = second

    # if i75.switch_pressed(SWITCH_A):
    #     if not switch_a_pressed:
    #         set_brightness(graphics, -10)
    #     switch_a_pressed = True
    # else:
    #     switch_a_pressed = False

    # if i75.switch_pressed(SWITCH_B):
    #     if not switch_b_pressed:
    #         set_brightness(graphics, 10)
    #     switch_b_pressed = True
    # else:
    #     switch_b_pressed = False
