import pygame

window = pygame.display.set_mode((920, 720))
pygame.display.set_caption('Chinese Checkers FCAI')

board_width = 480  # width of the board
checkers_distance = 40  # distance between the board and the checkers

board_positions_list = []  # arr of all the positions of the board
previous_move = []  # arr of the previous move
ai_pieces = []  # arr of arr_checkers checkers for each player (AI and Human)
human_pieces = []  # arr of checkers that are in the same row

# colors used for the board
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 200)
red = (200, 0, 0)
light_red = (255, 0, 0)
light_blue = (0, 0, 255)
pink = (255, 200, 200)
dark_green = (0, 100, 0)
light_green = (0, 255, 0)
yellow = (255, 255, 0)
light_yellow = (255, 255, 200)
light_purple = (200, 200, 255)
purple = (200, 0, 200)
light_pink = (255, 200, 255)
dark_grey = (50, 50, 50)
light_grey = (150, 150, 150)
dark_red = (150, 0, 0)
