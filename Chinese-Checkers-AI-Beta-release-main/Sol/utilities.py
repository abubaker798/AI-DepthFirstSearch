# y to the furthest end
def y_to_win(player, checkers):
    distance = 0
    if player == "human":  # distance to 680
        for i in range(10):
            distance += abs(680 - checkers[i].pos[1])
    else:  # distance to 40
        for i in range(10):
            distance += abs(checkers[i].pos[1] - 40)

    return distance


# horizontal distance to middle line
def distance_to_mid_board(checkers): # checkers is a list of checkers
    distance = 0 # distance to middle line (horizontal) for each checker
    for i in range(10): # for each checker in the list of checkers (10)
        distance += abs(checkers[i].pos[0] - 480) # add distance to middle line to distance variable (absolute value) (480 is the middle line)

    return distance


# vertical advance towards goal
def vertical_moves(self, opponent):
    move_distance = 0
    self_list = [] # list of current positions
    opponent_list = [] # list of opponent positions
    for i in range(len(self)): # for each checker in the list of checkers (10)
        self_list.append(self[i].pos) # add current position to list of current positions
    for i in range(len(opponent)): # for each checker in the list of checkers (10)
        opponent_list.append(opponent[i].pos) # add current position to list of current positions
    for i in range(10): # for each checker in the list of checkers (10)
        self[i].moves = [] # reset moves
        self[i].legal_moves(self[i].pos, False, 0, self_list, opponent_list) # get legal moves for each checker (10)
        move_distance += abs(self[i].best_vertical_move() - self[i].pos[1]) # add vertical distance to move_distance variable (absolute value)

    return move_distance


def create_set(arr):
    s = set([])
    for i in range(len(arr)):
        s.add(arr[i])
    return s


def is_won(current, terminal):  # check if the game is over
    current_list = []  # list of current positions
    terminal_list = []  # list of arr_checkers positions
    for i in range(10):
        current_list.append(current[i].pos)
        terminal_list.append(terminal[i].pos)
    return create_set(current_list) == create_set(terminal_list)


