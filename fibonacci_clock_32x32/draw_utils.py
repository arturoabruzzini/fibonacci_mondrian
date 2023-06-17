WHITE = None
BLACK = None
RED = None
YELLOW = None
BLUE = None
colour_map = None

def set_draw_utils(graphics):
    global WHITE, BLACK, RED, YELLOW, BLUE, colour_map
    # set up some pens to use later
    WHITE = graphics.create_pen(255, 255, 255)
    BLACK = graphics.create_pen(0, 0, 0)
    RED = graphics.create_pen(255, 0, 0)
    YELLOW = graphics.create_pen(255, 255, 0)
    BLUE = graphics.create_pen(0, 0, 255)

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


def draw_rect(graphics, x, y, size, colour):
    graphics.set_pen(colour_map[colour])
    graphics.rectangle(x, y, size, size)