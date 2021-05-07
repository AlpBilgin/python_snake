import random
import sys

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

def _test():
    res = snake_state(16)
    sys.stdout.write(''.join(res[0]))
    sys.stdout.write(res[1])

if __name__ == '__main__':
    _test()
