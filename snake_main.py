from snake_lib.console_draw import console_draw
from snake_lib.snake_state import snake_state, possible_directions, possible_states, start_dir_head_state_map

import time
import sys

cells = 100
root = 10

(starting_states,current_direction,head) = snake_state(cells)

tail=head


alive = True
while alive:
    time.sleep(0.01)
    # detect arrow
    ch = sys.stdin.read(3)
    if ch=='\x1b[A':
        current_direction = possible_directions[0] #up
    elif ch=='\x1b[B':
        current_direction = possible_directions[2] #down
    elif ch=='\x1b[C':
        current_direction = possible_directions[1] #right
    elif ch=='\x1b[D':
        current_direction = possible_directions[3] #left
    else:
        console_draw("not an arrow key!")
        continue
    # store current head index as last head index
    last_head = head
    # move head index in current direction
    # if index is occupied
    ## if not food die
    ## toggle growth flag
    # convert head index to horizontal or vertical bar depending on current direction
    # convert last head index to a bend if current head and last head don't match
    # if growth flag is not tagged
    ## store current tail index as last tail index
    ## move tail index according to tail shape
    ## erase last tail index
    
    linear = ''.join(starting_states)




    console_draw(linear,root)
    
console_draw('demo end')