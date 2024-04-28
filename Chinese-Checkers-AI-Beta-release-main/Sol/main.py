import math
import sys
import time

import pygame.font

import minimax
from board import *


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text, x, y, size):
    largeText = pygame.font.SysFont('system', size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    window.blit(TextSurf, TextRect)

    pygame.display.update()


def game_over(winner):
    if winner is human:
        message_display('You win!', 790, 110, 60)
    else:
        message_display('You lose!', 790, 110, 60)


def button(text, x, y, w, h, color, highlight_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(window, color, (x, y, w, h))
        if click[0] == 1 and action is not None:
            if action == "Start":
                game_loop()
            elif action == "Exit":
                pygame.quit()
                sys.exit()
            elif action == "Difficulty 1":
                minimax.max_depth = 1
                game_loop()
            elif action == "Difficulty 2":
                minimax.max_depth = 2
                game_loop()
            elif action == "Difficulty 3":
                minimax.max_depth = 5
                game_loop()
    else:
        pygame.draw.rect(window, highlight_color, (x, y, w, h))

    smallText = pygame.font.SysFont('system', 20)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    window.blit(TextSurf, TextRect)


def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill(light_yellow)
        largeText = pygame.font.SysFont('system', 50)
        TextSurf, TextRect = text_objects("Chinese Checkers FCAI project", largeText)
        TextRect.center = (920 / 2, 200)
        window.blit(TextSurf, TextRect)

        button("Exit", 800, 659, 110, 60, light_purple, purple, "Exit")
        button("Difficulty easy", 150, 440, 180, 60, dark_grey, light_grey, "Difficulty 1")
        button("Difficulty normal", 370, 440, 180, 60, dark_grey, light_grey, "Difficulty 2")
        button("Difficulty hard", 590, 440, 180, 60, dark_grey, light_grey, "Difficulty 3")

        pygame.display.update()


def game_loop():
    draw_board()
    create_pieces()
    selected_piece = None
    turn = 0
    human_turns = 0

    while True:
        move_string = "move count: " + str(human_turns)
        window.fill(light_yellow, (30, 140, 150, 40))
        message_display(move_string, 100, 150, 20)
        window.fill(light_yellow, (20, 180, 170, 40))
        button("Retry", 60, 60, 110, 60, light_pink, pink)
        button("Exit", 170, 60, 110, 60, light_purple, purple)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and turn == 0:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] < 300 and mouse_pos[1] < 100:
                    button("Retry", 60, 60, 110, 60, light_pink, pink, "Start")
                    button("Exit", 170, 60, 110, 60, light_purple, purple, "Exit")

                if selected_piece is None:
                    for i in range(len(human.checkers)):
                        if math.sqrt(math.pow(mouse_pos[0] - human.checkers[i].pos[0], 2) + math.pow(
                                mouse_pos[1] - human.checkers[i].pos[1], 2)) < 20:
                            human.checkers[i].selected()
                            selected_piece = human.checkers[i]
                            break
                else:
                    for i in range(len(board_positions_list)):
                        if math.sqrt(math.pow(mouse_pos[0] - selected_piece.pos[0], 2) + math.pow(
                                mouse_pos[1] - selected_piece.pos[1], 2)) < 20:
                            selected_piece.deselect()
                            selected_piece = None
                            break
                        if math.sqrt(
                                math.pow(mouse_pos[0] - board_positions_list[i][0], 2) + math.pow(
                                    mouse_pos[1] - board_positions_list[i][1],
                                    2)) < 20:
                            if board_positions_list[i] in selected_piece.moves:
                                selected_piece.move(board_positions_list[i])
                                human_turns += 1
                                if is_won(human.checkers, human_pieces):
                                    game_over(human)
                                else:
                                    selected_piece = None
                                    turn = 1
                            break

            elif turn == 1:  # ai's turn to make a move
                ai.make_move()
                turn = 0
                if is_won(ai.checkers, ai_pieces):  # check if ai won
                    game_over(ai)
                    time.sleep(3)
                    main_menu()

        pygame.display.update()


pygame.init()
make_board()
main_menu()
game_loop()
pygame.quit()
sys.exit()
