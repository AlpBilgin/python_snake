from snake_lib.console_draw import console_draw
from snake_lib.snake_state import snake_state, possible_directions, possible_states, start_dir_head_state_map

import time
import sys
import keyboard

cells = 100
root = 10

(board,current_direction,head,starting_head) = snake_state(cells)

if current_direction == possible_directions[0]:
    offset = -root
elif current_direction == possible_directions[1]:
    offset = 1
elif current_direction == possible_directions[2]:
    offset = root
else: 
    offset = -1

tail=head
last_head=head
head_state = starting_head
alive = True
growth = False

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
    # convert head index to horizontal or vertical bar depending on current direction
    board[head] = head_state
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
    ## store current tail index as last tail index
    ## move tail index according to tail shape
    ## erase last tail index
    
    linear = ''.join(board)
    console_draw(linear,root)
    
