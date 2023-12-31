from draw_utils import *

fibonacci_all = [1, 1]
while fibonacci_all[-1] < 34:
    fibonacci_all.append(fibonacci_all[-1] + fibonacci_all[-2])

fibonacci = fibonacci_all[1:]

quadrant_coords = [
    [21+8+1, 13+2],
    [21+8, 13+2],
    [21+8, 13],
    [21+8+2, 13],
    [21+8, 13+3],
    [21, 13],
    [21, 0],
    [21+13, 0],
    [21, 21],
]

# flip y axis
quadrant_coords_min = quadrant_coords[:]
for i in range(len(quadrant_coords_min)):
    quadrant_coords_min[i] = [quadrant_coords_min[i][0],
                              55-fibonacci_all[i]-quadrant_coords_min[i][1]]

minutes_config = {
    'coords': quadrant_coords_min,
    'colour': ['red', 'blue', 'blue', 'blue', 'yellow', 'yellow', 'red', 'red', 'blue']
}

# switch x and y, then flip y axis
quadrant_coords_h = quadrant_coords[:]
for i in range(len(quadrant_coords_h)):
    # quadrant_coords_h[i] = list(reversed(quadrant_coords_h[i]))
    quadrant_coords_h[i] = [quadrant_coords_h[i][1],
                            55-fibonacci_all[i]-quadrant_coords_h[i][0]]

hours_config = {
    'coords': quadrant_coords_h[:-1],
    'colour': ['yellow', 'blue', 'blue', 'blue', 'red', 'red', 'yellow', 'yellow']
}


def decimal_to_fibonary(decimal_num):
    # Convert the decimal number to modified Fibonacci binary
    fibonary = ""
    for num in reversed(fibonacci):
        if decimal_num >= num:
            fibonary += '1'
            decimal_num -= num
        else:
            fibonary += '0'

    # Pad the modified Fibonacci fibonary number to 8 digits
    fibonary = "{:0>8}".format(fibonary)

    return fibonary


def get_fibonary_time(hour, minute):
    return {
        'quadrant': fibonacci,
        'hours': list(reversed(decimal_to_fibonary(hour))),
        'minutes': list(reversed(decimal_to_fibonary(minute))),
    }


canvas_size = 55
border_size = 0
colour_all_quadrants = False


def draw_fibonacci(graphics, hour, minute, offset_x, offset_y, invert=False):
    quadrants = get_fibonary_time(hour, minute)
    # print('Hours ' + "".join(quadrants['hours']))
    # print('Minutes ' + "".join(quadrants['minutes']))

    # draw minutes
    for index in range(len(minutes_config['coords'])):
        x, y = minutes_config['coords'][index]
        active = quadrants['minutes'][index] if index == 0 else quadrants['minutes'][index-1]
        colour_to_use = minutes_config['colour'][index] if (
            active == '1' or colour_all_quadrants) else 'white'
        draw_square(graphics, x + offset_x, y + offset_y,
                    fibonacci_all[index], colour_to_use, invert)

    # draw hours
    for index in range(len(hours_config['coords'])):
        x, y = hours_config['coords'][index]
        active = quadrants['hours'][index] if index == 0 else quadrants['hours'][index-1]
        colour_to_use = hours_config['colour'][index] if (
            active == '1' or colour_all_quadrants) else 'white'
        draw_square(graphics, x + offset_x, y + offset_y,
                    fibonacci_all[index], colour_to_use, invert)
