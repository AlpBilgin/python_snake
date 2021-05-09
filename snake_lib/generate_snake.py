
# snake is designed to fall somewhere in the center but is biased
def generate_snake(size: int, width: int):
    snake = []
    start = int((size+width)/2)
    snake.append(start)
    return snake


def _test():
    snake = generate_snake(16, 4)
    assert(snake[0] == 10)
    print('generate_snake test passed')


if __name__ == '__main__':
    _test()
