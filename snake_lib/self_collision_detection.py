def self_collision_detection(snake: list):
    if len(snake) == 1:
        return False
    if snake[0] in snake[1:]:
        return True
    return False


def _test():
    assert(not self_collision_detection([4]))
    assert(self_collision_detection([4, 4]))
    assert(not self_collision_detection([4, 5]))
    assert(self_collision_detection([4, 5, 4]))
    assert(not self_collision_detection([4, 5, 6]))
    print('self_collision_detection test passed')


if __name__ == '__main__':
    _test()
