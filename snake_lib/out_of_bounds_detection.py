# size and widht could be initialised, left and right columns could be precalculated and used for quick lookup
def out_of_bounds_detection(snake: list, size: int, width: int):
    if snake[0] < 0 or snake[0] > size:
        return True
    if (snake[0] == snake[1]+1 and snake[0] % width == 0 and snake[1] % width == width-1) or (snake[0]+1 == snake[1] and snake[0] % width == width-1 and snake[1] % width == 0): # checks if head and last head are disjoint
        return True
    return False


def _test():
    assert(out_of_bounds_detection([-1, 0], 4, 2))
    assert(out_of_bounds_detection([4, 3], 4, 2))
    assert(out_of_bounds_detection([1, 2], 4, 2))
    assert(out_of_bounds_detection([2, 1], 4, 2))
    assert(not out_of_bounds_detection([1, 0], 4, 2))
    assert(not out_of_bounds_detection([0, 1], 4, 2))
    assert(not out_of_bounds_detection([2, 3], 4, 2))
    assert(not out_of_bounds_detection([3, 2], 4, 2))

    print('out_of_bounds_detection test passed')


if __name__ == '__main__':
    _test()
