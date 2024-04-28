from constants import *
from minimax import *


class Player:
    def __init__(self, color):
        self.color = color
        self.checkers = []

    def make_move(self):
        move = mini_max(self.checkers, ai_pieces, human_pieces, human.checkers)
        target = move[0]
        new_pos = move[1] # new position of the checker
        pygame.draw.circle(window, light_yellow, target.pos, 20, 0)
        pygame.draw.circle(window, black, target.pos, 20, 1)
        pygame.draw.circle(window, red, new_pos.pos, 20, 0)
        for i in range(10):
            if self.checkers[i].pos == target.pos:
                self.checkers[i] = new_pos
        print("MiniMax has made a move")


human = Player(dark_green)
ai = Player(red)


class ChineseChecker:

    def __init__(self, pos):
        self.pos = pos  # position of checker
        self.moves = []  # possible moves

    def render(self, color):  # renders the checker on the board
        pygame.draw.circle(window, color, self.pos, 20, 0)

    def selected(self):  # selects the checker and displays possible moves
        pygame.draw.circle(window, dark_red, self.pos, 20, 0)
        # show possible moves
        human_list = []
        ai_list = []
        for i in range(len(human.checkers)):
            human_list.append(human.checkers[i].pos)
        for i in range(len(ai.checkers)):
            ai_list.append(ai.checkers[i].pos)

        self.moves = []
        self.legal_moves(self.pos, False, 0, ai_list, human_list)

        for i in range(len(self.moves)):
            pygame.draw.circle(window, light_green, self.moves[i], 20, 0)
            pygame.draw.circle(window, black, self.moves[i], 20, 1)

    def deselect(self):  # deselects the checker
        pygame.draw.circle(window, dark_green, self.pos, 20, 0)
        for i in range(len(self.moves)):
            pygame.draw.circle(window, light_yellow, self.moves[i], 20, 0)
            pygame.draw.circle(window, black, self.moves[i], 20, 1)

    def move(self, new_pos):  # move to new position and remove old position
        pygame.draw.circle(window, light_yellow, self.pos, 20, 0)
        pygame.draw.circle(window, black, self.pos, 20, 1)
        pygame.draw.circle(window, dark_green, new_pos, 20, 0)
        self.pos = new_pos
        for i in range(len(self.moves)):
            if self.moves[i] != new_pos:
                pygame.draw.circle(window, light_yellow, self.moves[i], 20, 0)
                pygame.draw.circle(window, black, self.moves[i], 20, 1)
        self.moves = []

    def move_top_left(self, x_pos, y_pos, ai_list, human_list, hop):
        if is_empty((x_pos - 22, y_pos - 40), ai_list, human_list) and hop is False:
            self.moves.append((x_pos - 22, y_pos - 40))
        elif ((x_pos - 22, y_pos - 40) in human_list or (x_pos - 22, y_pos - 40) in ai_list) and (
                x_pos - 22, y_pos - 40) not in previous_move:
            previous_move.append((x_pos - 22, y_pos - 40))
            if is_empty((x_pos - 22 * 2, y_pos - 40 * 2), ai_list, human_list):
                self.moves.append((x_pos - 22 * 2, y_pos - 40 * 2))
                self.legal_moves((x_pos - 22 * 2, y_pos - 40 * 2), True, 1, ai_list, human_list)

    def move_top_right(self, x_pos, y_pos, ai_list, human_list, hop):
        if is_empty((x_pos + 22, y_pos - 40), ai_list, human_list) and hop is False:
            self.moves.append((x_pos + 22, y_pos - 40))
        elif ((x_pos + 22, y_pos - 40) in human_list or (x_pos + 22, y_pos - 40) in ai_list) and (
                x_pos + 22, y_pos - 40) not in previous_move:
            previous_move.append((x_pos + 22, y_pos - 40))
            if is_empty((x_pos + 22 * 2, y_pos - 40 * 2), ai_list, human_list):
                self.moves.append((x_pos + 22 * 2, y_pos - 40 * 2))
                self.legal_moves((x_pos + 22 * 2, y_pos - 40 * 2), True, 1, ai_list, human_list)

    def move_bottom_left(self, x_pos, y_pos, ai_list, human_list, hop):
        if is_empty((x_pos - 22, y_pos + 40), ai_list, human_list) and hop is False:
            self.moves.append((x_pos - 22, y_pos + 40))
        elif ((x_pos - 22, y_pos + 40) in human_list or (x_pos - 22, y_pos + 40) in ai_list) and (
                x_pos - 22, y_pos + 40) not in previous_move:
            previous_move.append((x_pos - 22, y_pos + 40))
            if is_empty((x_pos - 22 * 2, y_pos + 40 * 2), ai_list, human_list):
                self.moves.append((x_pos - 22 * 2, y_pos + 40 * 2))
                self.legal_moves((x_pos - 22 * 2, y_pos + 40 * 2), True, 1, ai_list, human_list)

    def move_bottom_right(self, x_pos, y_pos, ai_list, human_list, hop):
        if is_empty((x_pos + 22, y_pos + 40), ai_list, human_list) and hop is False:
            self.moves.append((x_pos + 22, y_pos + 40))
        elif ((x_pos + 22, y_pos + 40) in human_list or (x_pos + 22, y_pos + 40) in ai_list) and (
                x_pos + 22, y_pos + 40) not in previous_move:
            previous_move.append((x_pos + 22, y_pos + 40))
            if is_empty((x_pos + 22 * 2, y_pos + 40 * 2), ai_list, human_list):
                self.moves.append((x_pos + 22 * 2, y_pos + 40 * 2))
                self.legal_moves((x_pos + 22 * 2, y_pos + 40 * 2), True, 1, ai_list, human_list)

    def move_right(self, x_pos, y_pos, ai_list, human_list, hop):
        if is_empty((x_pos + 44, y_pos), ai_list, human_list) and hop is False:
            self.moves.append((x_pos + 44, y_pos))
        elif ((x_pos + 44, y_pos) in human_list or (x_pos + 44, y_pos) in ai_list) and (
                x_pos + 44, y_pos) not in previous_move:
            previous_move.append((x_pos + 44, y_pos))
            if is_empty((x_pos + 44 * 2, y_pos), ai_list, human_list):
                self.moves.append((x_pos + 44 * 2, y_pos))
                self.legal_moves((x_pos + 44 * 2, y_pos), True, 1, ai_list, human_list)

    def move_left(self, x_pos, y_pos, ai_list, human_list, hop):
        if is_empty((x_pos - 44, y_pos), ai_list, human_list) and hop is False:
            self.moves.append((x_pos - 44, y_pos))
        elif ((x_pos - 44, y_pos) in human_list or (x_pos - 44, y_pos) in ai_list) and (
                x_pos - 44, y_pos) not in previous_move:
            previous_move.append((x_pos - 44, y_pos))
            if is_empty((x_pos - 44 * 2, y_pos), ai_list, human_list):
                self.moves.append((x_pos - 44 * 2, y_pos))
                self.legal_moves((x_pos - 44 * 2, y_pos), True, 1, ai_list, human_list)

    def legal_moves(self, pos, hop, mode, ai_list,
                    human_list):  # mode = 1 for ai, mode = 2 for human player (hop = True for hop)
        global previous_move  # arr of the previous move
        if mode == 0:  # if the checker is not a king
            previous_move = []  # reset the previous move arr

        x_pos = pos[0]  # x coordinate of the checker
        y_pos = pos[1]  # y coordinate of the checker

        # move top left
        self.move_top_left(x_pos, y_pos, ai_list, human_list, hop)

        # move top right
        self.move_top_right(x_pos, y_pos, ai_list, human_list, hop)

        # move left
        self.move_left(x_pos, y_pos, ai_list, human_list, hop)

        # move right
        self.move_right(x_pos, y_pos, ai_list, human_list, hop)

        # move down left
        self.move_bottom_left(x_pos, y_pos, ai_list, human_list, hop)

        # move down right
        self.move_bottom_right(x_pos, y_pos, ai_list, human_list, hop)

    def best_vertical_move(self):  # returns the best vertical move for the AI to make
        if self is human:  # if the AI is the human player (the one who is playing)
            ai_max = 0
            for i in range(len(self.moves)):
                if self.moves[i][1] > ai_max: # if the y coordinate of the move is higher than the current max
                    ai_max = self.moves[i][1]
            return ai_max
        else:  # if the AI is the computer player
            ai_min = 600
            for i in range(len(self.moves)):
                if self.moves[i][1] < ai_min: # if the y coordinate of the move is lower than the current min
                    ai_min = self.moves[i][1]
            return ai_min


def make_board():
    for i in range(0, 4):  # 4 rows
        for j in range(i + 1):  # 4 columns
            board_positions_list.append(
                (board_width - 22 * i + 44 * j, checkers_distance * (i + 1)))  # add to board_positions_list
    for i in range(4, 9):  # 5 rows
        for j in range(17 - i):  # 18 columns
            board_positions_list.append(
                (board_width - 22 * (16 - i) + 44 * j, checkers_distance * (i + 1)))  # add to board_positions_list
    for i in range(9, 13):  # 3 rows
        for j in range(i + 1):  # 4 columns
            board_positions_list.append(
                (board_width - 22 * i + 44 * j, checkers_distance * (i + 1)))  # add to board_positions_list
    for i in range(13, 17):  # 3 rows
        for j in range(17 - i):  # 18 columns
            board_positions_list.append(
                (board_width - 22 * (16 - i) + 44 * j, checkers_distance * (i + 1)))  # add to board_positions_list


def draw_board():
    window.fill(light_yellow)
    for i in range(len(board_positions_list)):
        pygame.draw.circle(window, black, board_positions_list[i], 20, 1)


def create_pieces():
    global ai_pieces, human_pieces

    for i in range(10):
        piece = ChineseChecker(board_positions_list[i])
        ai_pieces.append(piece)
    for i in reversed(range(len(board_positions_list) - 10, len(board_positions_list))):
        piece = ChineseChecker(board_positions_list[i])
        human_pieces.append(piece)

    human.checkers = []
    ai.checkers = []
    for i in range(10):
        piece = ChineseChecker(board_positions_list[i])
        piece.render(human.color)
        human.checkers.append(piece)
    for i in reversed(range(len(board_positions_list) - 10, len(board_positions_list))):
        piece = ChineseChecker(board_positions_list[i])
        piece.render(ai.color)
        ai.checkers.append(piece)


def is_empty(pos, ai_list, human_list):
    if pos in board_positions_list and pos not in human_list and pos not in ai_list:
        return True
    else:
        return False


def is_mixed():  # returns true if the board is mixed (not all the same highlight_color) and false if it is not mixed (all the same highlight_color)
    human_max = 0  # find the largest y
    ai_min = 600  # max y
    human_min = 600  # min y
    ai_max = 0  # min y

    for i in range(10):
        if human.checkers[i].pos[1] > human_max:
            human_max = human.checkers[i].pos[1]
        if ai.checkers[i].pos[1] < ai_min:
            ai_min = ai.checkers[i].pos[1]

    for i in range(10):
        if human.checkers[i].pos[1] < human_min:
            human_min = human.checkers[i].pos[1]
        if ai.checkers[i].pos[1] > ai_max:
            ai_max = ai.checkers[i].pos[1]

    if (human_min < ai_min and (ai_min - human_max) > 120) or (
            ai_min < human_min and (human_min - ai_max) > 0):  # no interactions
        return False
    else:
        return True
