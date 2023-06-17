from interstate75 import Interstate75, DISPLAY_INTERSTATE75_32X32

i75 = Interstate75(display=DISPLAY_INTERSTATE75_32X32)
graphics = i75.display

width = i75.width
height = i75.height

# set up some pens to use later
WHITE = graphics.create_pen(255, 255, 255)
BLACK = graphics.create_pen(0, 0, 0)

graphics.set_font("bitmap8")


def draw_text(text, x, y):
    # # function for drawing outlined text
    # graphics.set_pen(BLACK)
    # graphics.text(text, x - 1, y - 1, -1, 1)
    # graphics.text(text, x, y - 1, -1, 1)
    # graphics.text(text, x + 1, y - 1, -1, 1)
    # graphics.text(text, x - 1, y, -1, 1)
    # graphics.text(text, x + 1, y, -1, 1)
    # graphics.text(text, x - 1, y + 1, -1, 1)
    # graphics.text(text, x, y + 1, -1, 1)
    # graphics.text(text, x + 1, y + 1, -1, 1)
    graphics.set_pen(WHITE)
    graphics.text(text, x, y, -1, 1)
