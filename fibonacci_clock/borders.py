from draw_utils import *

border_size = 4
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


def draw_borders(graphics, second, offset_x, offset_y, invert=False):
    # draw border
    for x, y, width, height, colour in border_config:
        draw_rect(graphics, x + offset_x, y + offset_y,
                  width, height, colour, invert)

    # add black square to show seconds progress
    if False:
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

    # clip border to show seconds progress
    if False:
        if second > 0:
            max_width_top = border_size_sm + 55
            progress_top = min(second * 4, max_width_top)
            if progress_top > max_width_top / 2 and progress_top < max_width_top:
                progress_top -= 1
            draw_rect(
                graphics,
                -border_size_sm + progress_top + offset_x,
                -border_size_sm + offset_y,
                (max_width_top - progress_top),
                border_size_sm,
                'black',
                invert)

            max_height_right = border_size_sm + 55 + border_size
            progress_right = min((second - 15) * 4, max_height_right)
            if progress_right > max_height_right / 2 and progress_right < max_height_right:
                progress_right -= 1
            draw_rect(
                graphics,
                55 + offset_x,
                -border_size_sm + progress_right + offset_y,
                border_size,
                (max_height_right - progress_right),
                'black',
                invert)

            max_width_bottom = border_size_sm + 55
            progress_bottom = min((second - 31) * 4, max_width_bottom)
            if progress_bottom > max_width_bottom / 2 and progress_bottom < max_width_bottom:
                progress_bottom -= 1
            draw_rect(
                graphics,
                -border_size_sm + offset_x,
                55 + offset_y,
                (max_width_bottom - progress_bottom),
                border_size_sm,
                'black',
                invert)

            max_height_left = 55
            progress_left = min((second - 46) * 4, max_height_left)
            if progress_left > max_height_left / 2 and progress_left < max_height_left:
                progress_left -= 1
            draw_rect(
                graphics,
                -border_size_sm + offset_x,
                offset_y,
                border_size_sm,
                (max_height_left - progress_left),
                'black',
                invert)
