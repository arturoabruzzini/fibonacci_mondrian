from draw_utils import *

border_size = 5
border_size_sm = 4

border_config = [
    # top
    [-border_size_sm, -border_size_sm, border_size_sm + 8, border_size_sm, 'white'],
    [8, -border_size_sm, 13, border_size_sm, 'blue'],
    [21, -border_size_sm, 21, border_size_sm, 'red'],
    [42, -border_size_sm, 13, border_size_sm, 'yellow'],

    # right
    [55, -border_size, border_size, border_size + 13, 'white'],
    [55, 13, border_size, 21, 'red'],
    [55, 34, border_size, 13, 'yellow'],
    [55, 47, border_size, 8 + border_size, 'blue'],

    # bottom
    [-border_size_sm, 55, border_size_sm + 8, border_size, 'red'],
    [8, 55, 26, border_size, 'yellow'],
    [34, 55, 8, border_size, 'blue'],
    [42, 55, 13, border_size, 'white'],

    # left
    [-border_size_sm, 0, border_size_sm, 13, 'red'],
    [-border_size_sm, 13, border_size_sm, 8, 'white'],
    [-border_size_sm, 21, border_size_sm, 26, 'yellow'],
    [-border_size_sm, 47, border_size_sm, 8, 'blue'],
]


def draw_borders(graphics, second, offset_x, offset_y, invert):
    # draw border
    for x, y, width, height, colour in border_config:
        draw_rect(graphics, x + offset_x, y + offset_y,
                  width, height, colour, invert)

    # clip border to show seconds progress
    x = - 4
    y = - 4
    width = 4
    height = 4
    if second < 15:
        progress = min(second, 15) / 15
        x = - 4 + int(60 * progress)

        if second >= 8:
            x = x - 1
    elif second <= 30:
        x = 55
        width = 5
        progress = min(second - 15, 15) / 15
        y = - 4 + int(60 * progress)

        if second == 30:
            height = 5

        if second >= 15 + 8:
            y = y - 1
    elif second <= 45:
        y = 55
        height = 5
        progress = min(second - 30, 15) / 15
        x = 55 - int(60 * progress)
        if second >= 30 + 8:
            x = x + 1
    else:
        x = - 4
        progress = min(second - 45, 15) / 15
        y = 55 - int(60 * progress)
        if second >= 45 + 8:
            y = y + 1

    draw_rect(graphics, x + offset_x, y + offset_y,
              width, height, 'black', invert)
