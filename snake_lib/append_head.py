from .snake_directions import snake_directions


def append_head(snake: list, width: int, current_direction: str):
    offset = 0
    if current_direction == snake_directions[0]:
        offset = -width
    elif current_direction == snake_directions[1]:
        offset = 1
    elif current_direction == snake_directions[2]:
        offset = width
    else:
        offset = -1
    snake.insert(0, snake[0]+offset)
    return snake


def _test():
    snake = [10]
    width = 8
    snake = append_head(snake, 4, 'u')
    assert(snake == [6, 10])
    append_head(snake, 4, 'r')
    append_head(snake, 4, 'd')
    append_head(snake, 4, 'l')


if __name__ == '__main__':
    _test()
