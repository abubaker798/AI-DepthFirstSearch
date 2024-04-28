import copy

from utilities import *


class Node:
    def __init__(self, checkers, path):
        self.checkers = checkers  # list of checkers in the current node (checkers)
        self.path = path  # path to the current node (checkers)

    def possible_action(self, ai, human):  # returns a list of possible possible_action for the current node (checkers)
        checker_states = []  # arr of arr, all 10 checkers states
        ai_list = []  # arr of all the possible moves for the AI
        human_list = []  # arr of all the possible moves for the Human
        for i in range(len(ai)):  # for each checker
            ai_list.append(
                ai[i].pos)  # add the current position of the checker to the list of possible moves for the AI
        for i in range(len(human)):  # for each checker
            human_list.append(
                human[i].pos)  # add the current position of the checker to the list of possible moves for the Human

        for i in range(10):
            self.checkers[i].moves = []  # reset the moves for each checker in the current node
            self.checkers[i].legal_moves(self.checkers[i].pos, False, 0, ai_list,
                                         human_list)  # get all the possible moves for the checker
            for j in range(len(self.checkers[i].moves)):  # for each possible move
                checker_list = copy.deepcopy(
                    self.checkers)  # copy the current checkers list to a new list of checkers (checker_list)
                checker_list[i].pos = self.checkers[i].moves[j]  # move the checker to the new position
                checker_states.append(checker_list)  # add the new checker state to the list of checker states
        return checker_states  # return the list of checker states


max_depth = 1  # max depth of the game tree


def mini_max(state, arr_checkers, players_checkers, enemy):  # get the best move for the current state of game tree
    print("max_depth:", max_depth)
    infinity = float('inf')  # infinity is a float value
    best_val = -infinity  # best value of current state of game tree
    temp_pos = None  # new position of the checker
    best_move = []  # arr of best moves
    node = Node(state, [state])  # create a node with current state of game tree
    successors = node.possible_action(state, enemy)  # arr of all the successors of the current state of game tree

    for child in successors:  # for each successor of the current state of game tree
        value = get_min(child, arr_checkers, players_checkers, enemy, 1)  # get the value of the successor
        if value > best_val:  # if the value of the successor is greater than the best value of the current state of game tree
            best_val = value  # set the best value of the current state of game tree to the value of the successor
            temp_pos = child  # set the new position of the checker to the successor
    for i in range(10):  # for each checker
        if temp_pos[i].pos != state[i].pos:  # if the new position of the checker is different from the current position
            best_move.append(state[i])  # add the checker to the best moves
            best_move.append(temp_pos[i])  # add the new position of the checker to the best moves

    return best_move  # return the best moves


def get_max(state, arr_checkers, players_checkers, opponent,
            depth):  # get the max value of the current state of game tree
    if choice_test(state, arr_checkers) or choice_test(opponent,
                                                       players_checkers) or depth >= max_depth:  # test if the current state of game tree is terminal
        d = evaluate_move(state, opponent, arr_checkers, players_checkers)
        return d  # return utility value of current state of game tree
    infinity = float('inf')
    value = -infinity
    node = Node(state, [state])  # create a node with current state of game tree
    successors = node.possible_action(state, opponent)  # arr of all the successors of the current state of game tree
    for child in successors:  # for each successor of the current state of game tree
        value = max(value, get_min(child, arr_checkers, players_checkers, opponent,
                                   depth + 1))  # get the value of the successor of the current state of game tree
    return value  # return the max value of the current state of game tree


def get_min(state, arr_checkers, players_checkers, opponent, depth):
    if choice_test(state, arr_checkers) or choice_test(opponent, players_checkers) or depth >= max_depth:
        d = evaluate_move(state, opponent, arr_checkers,
                          players_checkers)  # evaluate the move of the current state of game tree
        return d  # return utility value of current state of game tree
    infinity = float('inf')  # infinity is a float value
    value = infinity  # value is the best value of the current state of game tree
    node = Node(opponent, [opponent])  # create a node with current state of game tree
    successors = node.possible_action(opponent, state)  # arr of all the successors of the current state of game tree
    for child in successors:  # for each successor of the current state of game tree
        value = min(value,
                    get_max(child, arr_checkers, players_checkers, state, depth + 1))  # get the value of the successor
    return value  # return the value of the current state of game tree


def evaluate_move(ai_checkers, human_checkers, ai_terminal, human_terminal): # evaluate the move
    # of the current state of game tree and return the utility value of the current state of game tree
    value = 0.6 * (y_to_win("human", human_checkers) - y_to_win("ai", ai_checkers)) + 0.3 * (
            distance_to_mid_board(human_checkers) - distance_to_mid_board(ai_checkers)) + 0.4 * (
                    vertical_moves(ai_checkers, human_checkers) - vertical_moves(human_checkers, ai_checkers))
    return value


def choice_test(state, terminal):  # test if the current state of game tree is terminal
    s = create_set(state)  # create a set of the current state of game tree
    t = create_set(terminal)  # create a set of the terminal state of game tree
    return s == t  # return if the current state of game tree is terminal
