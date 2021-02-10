import copy
print("Enter the initial state:\n")
# initializing an empty matrix
initial_state = []
# taking 3x3 matrix from the user
for i in range(3):
   # empty row
   row = []
   for j in range(3):
      # asking the user to input the number
      # converts the input to int as the default one is string
      element = int(input())
      # appending the element to the 'row'
      row.append(element)
   # appending the 'row' to the 'matrix'
   initial_state.append(row)
# printing the matrix
print(initial_state)
   
#initial_state = [[1,2,3],[0,4,6],[7,5,8]]
# initial_state = [[4,0,6],[1,2,3],[7,5,8]]

print("Enter the goal state:\n")
goal_state = []
# taking 3x3 matrix from the user
for i in range(3):
   # empty row
   row = []
   for j in range(3):
      # asking the user to input the number
      # converts the input to int as the default one is string
      element = int(input())
      # appending the element to the 'row'
      row.append(element)
   # appending the 'row' to the 'matrix'
   goal_state.append(row)
# printing the matrix
print(goal_state)

#goal_state = [[1,2,3],[4,5,6],[7,8,0]]

def get_pos(state):
    for x, row in enumerate(state):
        for y, col in enumerate(row):
            if col == 0:
                return (x, y)

def h_func(curr_state, goal_state):
    h = 0
    for c, g in zip(curr_state, goal_state):
        for x, y in zip(c, g):
            if(y != x):
                h += 1
    return h

def print_state(state):
    print('-----')
    for s in state:
        print(*s)
    print('-----')

def move_tile(state, direction, zero_pos):
    curr_state = copy.deepcopy(state)
    x, y = zero_pos
    n = len(curr_state)
    if direction == 0 and x != 0:
        curr_state[x][y], curr_state[x-1][y] = curr_state[x-1][y], curr_state[x][y]
    elif direction == 1 and x != n-1:
        curr_state[x][y], curr_state[x+1][y] = curr_state[x+1][y], curr_state[x][y]
    elif direction == 2 and y != n-1:
        curr_state[x][y], curr_state[x][y+1] = curr_state[x][y+1], curr_state[x][y]
    elif direction == 3 and y != 0:
        curr_state[x][y], curr_state[x][y-1] = curr_state[x][y-1], curr_state[x][y]
    return curr_state

def print_direction(d):
    if d == 0:
        print('UP')
    elif d == 1:
        print('DOWN')
    elif d == 2:
        print('RIGHT')
    elif d == 3:
        print('LEFT')


def dfs(curr_state, goal_state, zero_pos):
    # for all the state possible find the best state using h value
    # Generate all possible next combination
    # Direction 0: up, 1: down, 2: right, 3: left
    next_state = None
    min_h = 10
    next_move = 0

    for d in range(4):
        state = move_tile(curr_state, d, zero_pos)
        if h_func(state, goal_state) < min_h:
            next_state = state
            min_h = h_func(next_state, goal_state)
            next_move = d
    print('-'*20)
    print_state(next_state)
    print('H:', min_h)
    print('Direction:', end=' ')
    print_direction(next_move)
    if min_h == 0:
        print('Goal State Reached.')
        print_state(next_state)
        return
    else:
        zero_pos = get_pos(next_state)
        dfs(next_state, goal_state, zero_pos)


if __name__ == '__main__':
    print('INITIAL STATE:')
    print_state(initial_state)
    # Direction = namedtuple(Direction, ['up', 'down', 'right', 'left'])

    print('\nStarting search using A* algorithm...')

    zero_pos = get_pos(initial_state)
    dfs(initial_state, goal_state, zero_pos)
