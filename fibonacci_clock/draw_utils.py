WHITE = None
BLACK = None
RED = None
YELLOW = None
BLUE = None
colour_map = None

brightness = 30
brightness_white = 30

def set_brightness(graphics, value):
    global brightness, brightness_white
    brightness = round(min(max(value, 0), 100))
    # print('Brightness set to', brightness)
    brightness_white = round(max(brightness - 0, 20))
    # print('White brightness set to', brightness_white)
    set_draw_utils(graphics)
    return brightness


def dim(val):
    return round(val * brightness / 100)


def set_draw_utils(graphics):
    global WHITE, BLACK, RED, YELLOW, BLUE, colour_map
    # set up some pens to use later
    white_val = round((255 * brightness_white) / 100)
    # print("white_val", white_val)
    WHITE = graphics.create_pen(white_val, white_val, white_val)
    BLACK = graphics.create_pen(0, 0, 0)
    RED = graphics.create_pen(dim(255), 0, 0)
    YELLOW = graphics.create_pen(dim(255), dim(255), 0)
    BLUE = graphics.create_pen(0, 0, dim(255))

    colour_map = {
        'white': WHITE,
        'black': BLACK,
        'red': RED,
        'yellow': YELLOW,
        'blue': BLUE,
    }

    graphics.set_font("bitmap8")


def clear_drawing(graphics):
    graphics.set_pen(BLACK)
    graphics.clear()


def draw_text(graphics, text, x, y, flip=False):
    graphics.set_font("sans")
    graphics.set_thickness(2)
    TEXT = graphics.create_pen(255, 255, 0)
    graphics.set_pen(TEXT)
    graphics.text(text, x, y, -1, 0.5, 180 if flip else 0)


def draw_wait_text(graphics):
    graphics.set_pen(WHITE)
    graphics.text("Wait", 65, 4, scale=1)
    graphics.text("for", 65, 12, scale=1)
    graphics.text("WIFI...", 65, 20, scale=1)


def draw_rect(graphics, x, y, width, height, colour, invert=False):
    x_to_use = x if not invert else 32 - x - width
    y_to_use = y if not invert else 64 - y - height
    graphics.set_pen(colour_map[colour])
    graphics.rectangle(x_to_use, y_to_use, width, height)


def draw_square(graphics, x, y, size, colour, invert=False):
    draw_rect(graphics, x, y, size, size, colour, invert)

