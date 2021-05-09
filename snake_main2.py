from snake_lib.append_head import append_head
from snake_lib.generate_snake import generate_snake
from snake_lib.food import food
from snake_lib.self_collision_detection import self_collision_detection
from snake_lib.out_of_bounds_detection import out_of_bounds_detection
from snake_lib.trim_tail import trim_tail

size = 100
width = 10
current_direction = 'l'

snake = generate_snake(size, width)
food = food(size)
food_collision = False

# get new direction based on keyboard input using hooks declared here

while True:
    # generate food outside of snake if food doesn't exist and is not being eaten in this frame
    if food.getFoodState()[0]:
        food.respawnFood()
        while food.getFoodState()[1] in snake:
            food.rerollFoodPosition()
    # insert a new head to 0 pos accoring to new direction
    snake = append_head(snake, width, current_direction)
    # do self collision detection, break if self collision
    if self_collision_detection(snake):
        break
    # check for out of bounds, break if out of bounds
    if out_of_bounds_detection(snake, size, width):
        break
    # check food collision, despawn food
    if snake[0] == food.getFoodState()[2]:
        food.foodIsEaten()
    else:  # else trim tail
        snake = trim_tail(snake)

    # render (encapsulate with cosmetic borders)
    # print
