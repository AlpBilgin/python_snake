from snake_lib.append_head import append_head
from snake_lib.generate_snake import generate_snake
from snake_lib.food import food
#from snake_lib.trim_tail import trim_tail

size = 100
width = 10
current_direction = 'l'

snake = generate_snake(size, width)
food = food(size)
food_collision = False

# get new direction based on keyboard input using hooks declared here

while True:
    # insert a new head to 0 pos accoring to new direction
    snake = append_head(snake, width, current_direction)
    # do collision detection, flag if food collision, break if self collision
    # check for out of bounds, break if out of bounds
    # if food collision not flagged, trim tail
    # if food collision flagged, despawn food
    # generate food outside of snake if food doesn't exist and is not being eaten in this frame
    if food.getFoodState()[0] and not food_collision :
        food.respawnFood()
        while food.getFoodState()[1] in snake:
            food.rerollFoodPosition()

    # render (encapsulate with cosmetic borders)
    # print
