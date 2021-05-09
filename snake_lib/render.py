from .food import food


def render(snake: list, food: food, size: int, width: int):
    raster = [' ']*size
    for segment in snake:
        raster[segment] = '@'
    if not food.getFoodState()[0]:
        raster[food.getFoodState()[1]] =  'O'
    outer_width = width+2
    vertical_bar = ['═']*outer_width
    top_vertical_bar = list(vertical_bar)
    bottom_vertical_bar = list(vertical_bar)
    top_vertical_bar[0] = '╔'
    top_vertical_bar[-1] = '╗'
    top_vertical_bar.append('\n')
    bottom_vertical_bar[0] = '╚'
    bottom_vertical_bar[-1] = '╝'
    bottom_vertical_bar.append('\n')
    raster = ''.join(raster)
    scan = '\n'.join('║' + raster[i:i+width] +
                     '║' for i in range(0, len(raster), width)) + '\n'
    scan = ''.join(top_vertical_bar) + scan
    scan = scan + ''.join(bottom_vertical_bar)
    return scan


def _test():
    output = render([2,3], (False,5), 16, 4)
    assert(output == '╔════╗\n║\u2001\u2001@@║\n║\u2001O\u2001\u2001║\n║\u2001\u2001\u2001\u2001║\n║\u2001\u2001\u2001\u2001║\n╚════╝\n') 
    print('render passed all tests!')


if __name__ == '__main__':
    _test()
