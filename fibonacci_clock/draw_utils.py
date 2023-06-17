WHITE = None
BLACK = None
RED = None
YELLOW = None
BLUE = None
colour_map = None

brightness = 50


def set_brightness(graphics, diff):
    global brightness
    brightness = min(max(brightness + diff, 0), 100)
    print('Brightness set to', brightness)
    set_draw_utils(graphics)


def dim(val):
    return round(val * brightness / 100)


def set_draw_utils(graphics):
    global WHITE, BLACK, RED, YELLOW, BLUE, colour_map
    # set up some pens to use later
    WHITE = graphics.create_pen(dim(255), dim(255), dim(255))
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


def draw_text(graphics, text, x, y):
    graphics.set_pen(WHITE)
    graphics.text(text, x, y, -1, 1)


def draw_wait_text(graphics):
    graphics.set_pen(WHITE)
    graphics.text("Wait", 1, 4, scale=1)
    graphics.text("for", 1, 12, scale=1)
    graphics.text("WIFI...", 1, 20, scale=1)


def draw_rect(graphics, x, y, size, colour, invert=False):
    x_to_use = x if not invert else 32 - x - size
    y_to_use = y if not invert else 64 - y - size
    graphics.set_pen(colour_map[colour])
    graphics.rectangle(x_to_use, y_to_use, size, size)
