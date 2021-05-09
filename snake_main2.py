import keyboard
import time
from snake_lib.snake_directions import snake_directions
from snake_lib.append_head import append_head
from snake_lib.generate_snake import generate_snake
from snake_lib.food import food
from snake_lib.self_collision_detection import self_collision_detection
from snake_lib.out_of_bounds_detection import out_of_bounds_detection
from snake_lib.trim_tail import trim_tail
from snake_lib.render import render
from snake_lib.console_dump import console_dump

size = 100
width = 10
current_direction = 'l'

snake = generate_snake(size, width)
food = food(size)
food_collision = False

def up(_):
    global current_direction
    current_direction = snake_directions[0]
   
def right(_):
    global current_direction
    current_direction = snake_directions[1]

def down(_):
    global current_direction
    current_direction = snake_directions[2]

def left(_):
    global current_direction
    current_direction = snake_directions[3]

keyboard.on_press_key("w", up)
keyboard.on_press_key("d", right)
keyboard.on_press_key("s", down)
keyboard.on_press_key("a", left)

# get new direction based on keyboard input using hooks declared here

while True:
    time.sleep(1)
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
    if snake[0] == food.getFoodState()[1]:
        food.foodIsEaten()
    else:  # else trim tail
        snake = trim_tail(snake)

    # render (encapsulate with cosmetic borders)
    rendered = render(snake, food, size, width)
    # print
    console_dump(rendered)

print('you died')