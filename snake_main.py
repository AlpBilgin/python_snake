from snake_lib.console_draw import console_draw
import time
import sys
import keyboard
from collections import deque
import random

possible_states = ['┃','━','┏','┓','┗','┛',' ','#']
possible_directions = ['u','r','d','l']
start_dir_head_state_map = {'u':'┃','r':'━','d':'┃','l':'━'}

def snake_state(size:int=49):
    starting_states = [' '] * size
    starting_direction = random.choice(possible_directions)
    starting_head = start_dir_head_state_map[starting_direction]
    starting_cell = int((size - (size%2))/2)
    starting_states[starting_cell] = starting_head
    return (starting_states,starting_direction,starting_cell,starting_head)

random.seed()

cells = 100
root = 10
snake=deque()

(board,current_direction,head,starting_head) = snake_state(cells)

if current_direction == possible_directions[0]:
    offset = -root
elif current_direction == possible_directions[1]:
    offset = 1
elif current_direction == possible_directions[2]:
    offset = root
else: 
    offset = -1



last_head=head
snake.append(head)
head_state = starting_head
alive = True
growth = False
food = False

def up(_):
    global current_direction
    global offset
    global head_state
    current_direction = possible_directions[0]
    offset = -root
    head_state=possible_states[0]

def right(_):
    global current_direction
    global offset
    global head_state
    current_direction = possible_directions[1]
    offset = 1
    head_state=possible_states[1]

def down(_):
    global current_direction
    global offset
    global head_state
    current_direction = possible_directions[2]
    offset = root
    head_state=possible_states[0]

def left(_):
    global current_direction
    global offset
    global head_state
    current_direction = possible_directions[3]
    offset = -1
    head_state=possible_states[1]

keyboard.on_press_key("w", up)
keyboard.on_press_key("d", right)
keyboard.on_press_key("s", down)
keyboard.on_press_key("a", left)

while alive:
    time.sleep(1)
    # store current head index as last head index
    last_last_head=last_head
    last_head = head
    # move head index in current direction
    head += offset
    # if index is occupied
    if board[head] != possible_states[6]:
        ## if not food die
        if board[head] != possible_states[7]:
            console_draw("you died")
            break
        else:
            ## toggle growth flag
            growth = True
            food = False
    # convert head index to horizontal or vertical bar depending on current direction
    board[head] = head_state
    # add new head pos to queue
    snake.append(head)
    # convert last head index to a bend if current head and last head don't match
    if(head_state != board[last_head]):
        if board[last_head] == '┃':
            if head < last_head:
                if head < last_last_head:
                    board[last_head] = '┓'
                else:
                    board[last_head] = '┛'
            else:
                if head < last_last_head:
                    board[last_head] = '┏'
                else:
                    board[last_head] = '┗'
        else:
            if head < last_head:
                if last_head < last_last_head:
                    board[last_head] = '┗'
                else:
                    board[last_head] = '┛'
            else:
                if last_head < last_last_head:
                    board[last_head] = '┏'
                else:
                    board[last_head] = '┓'
                
    # if growth flag is not tagged
    if not growth:    
        ## fetch oldest coord from queue, use it to blank the last cell
        board[snake.popleft()] = ' '
    if not food:
        ## try to insert food
        ## random index
        candidate = random.randrange(0,len(board))
        if board[candidate] == ' ':
            board[candidate] = '#'
            food = True

    growth = False
    linear = ''.join(board)
    console_draw(linear,root)
    
