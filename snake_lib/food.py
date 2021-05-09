import random

class food:
    def __init__(self, size: int):
        # body of the constructor
        self._isDespawned = True
        self._position = -1
        self._size = size

    def getFoodState(self):
        return (self._isDespawned, self._position)

    def foodIsEaten(self):
        self._isDespawned = True

    def respawnFood(self):
        self._isDespawned = False
        self.rerollFoodPosition()
        return self.getFoodState()
    
    def rerollFoodPosition(self):
        self._position = random.randrange(0, self._size)

def _test():
    test_food = food(1)
    assert(test_food.getFoodState() == (False, -1))
    assert(test_food.respawnFood() == (True, 0))
    assert(test_food.getFoodState() == (True, 0))
    print('food passed all tests!')

if __name__ == '__main__':
    _test()
