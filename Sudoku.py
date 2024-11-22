import pygame, sys
from sudoku_generator import *
from cell import *
from board import *

BG_COLOR = (173, 216, 230)
game_over = False


pygame.init()
pygame.key.set_repeat(1000,0)
screen = pygame.display.set_mode((405, 504))
pygame.display.set_caption("Sudoku")

def opening_Screen():
    background_image = pygame.image.load("background_Sudoku.jpg")
    screen.blit(background_image, (0, 0), (700, 100, 405, 504))
    welcome = "Welcome to Sudoku"
    intro = pygame.font.Font(None, 60)
    welcome_surf = intro.render(welcome, True, "black")
    welcome_rect = welcome_surf.get_rect(center=(202.5, 125))
    screen.blit(welcome_surf, welcome_rect)
    options = "Select Game Mode"
    options_1 = pygame.font.Font(None, 40)
    options_surf = options_1.render(options, True, "black")
    options_rect = options_surf.get_rect(center=(202.5, 300))
    screen.blit(options_surf, options_rect)
    difficulty = pygame.font.Font(None, 25)
    easy_text = "Easy"
    medium_text = "Medium"
    hard_text = "Hard"
    pygame.draw.line(screen, "orange", (30, 352), (120, 352), 3)
    pygame.draw.line(screen, "orange", (30, 352), (30, 402), 3)
    pygame.draw.line(screen, "orange", (30, 402), (120, 402), 3)
    pygame.draw.line(screen, "orange", (120, 352), (120, 402), 3)
    easy_surf = difficulty.render(easy_text, True, "white")
    end_rect = easy_surf.get_rect(center=(75, 377))
    screen.blit(easy_surf, end_rect)

    pygame.draw.line(screen, "orange", (155, 352), (245, 352), 3)
    pygame.draw.line(screen, "orange", (155, 352), (155, 402), 3)
    pygame.draw.line(screen, "orange", (155, 402), (245, 402), 3)
    pygame.draw.line(screen, "orange", (245, 352), (245, 402), 3)
    medium_surf = difficulty.render(medium_text, True, "white")
    end_rect = medium_surf.get_rect(center=(200, 377))
    screen.blit(medium_surf, end_rect)

    pygame.draw.line(screen, "orange", (280, 352), (370, 352), 3)
    pygame.draw.line(screen, "orange", (280, 352), (280, 402), 3)
    pygame.draw.line(screen, "orange", (280, 402), (370, 402), 3)
    pygame.draw.line(screen, "orange", (370, 352), (370, 402), 3)
    hard_surf = difficulty.render(hard_text, True, "white")
    end_rect = hard_surf.get_rect(center=(325, 377))
    screen.blit(hard_surf, end_rect)

def difficulty_selection(click_x, click_y):
    easy = (30, 352, 120, 402)
    medium = (155, 352, 245, 402)
    hard = (280, 352, 370, 402)

    if easy[0] < click_x < easy[2] and easy[1] < click_y < easy[3]:
        return "easy"

    if medium[0] < click_x < medium[2] and medium[1] < click_y < medium[3]:
        return "medium"

    if hard[0] < click_x < hard[2] and hard[1] < click_y < hard[3]:
        return "hard"

def in_game_screen():
    button_font = pygame.font.Font(None, 25)

    pygame.draw.line(screen, "orange", (30, 429), (120, 429), 3)
    pygame.draw.line(screen, "orange", (30, 429), (30, 479), 3)
    pygame.draw.line(screen, "orange", (30, 479), (120, 479), 3)
    pygame.draw.line(screen, "orange", (120, 429), (120, 479), 3)
    button1 = "Reset"
    button1_surf = button_font.render(button1, True, "white")
    end_rect = button1_surf.get_rect(center=(75, 454))
    screen.blit(button1_surf, end_rect)

    pygame.draw.line(screen, "orange", (155, 429), (245, 429), 3)
    pygame.draw.line(screen, "orange", (155, 429), (155, 479), 3)
    pygame.draw.line(screen, "orange", (155, 479), (245, 479), 3)
    pygame.draw.line(screen, "orange", (245, 429), (245, 479), 3)
    button2 = "Restart"
    button2_surf = button_font.render(button2, True, "white")
    end_rect = button2_surf.get_rect(center=(200, 454))
    screen.blit(button2_surf, end_rect)

    pygame.draw.line(screen, "orange", (280, 429), (370, 429), 3)
    pygame.draw.line(screen, "orange", (280, 429), (280, 479), 3)
    pygame.draw.line(screen, "orange", (280, 479), (370, 479), 3)
    pygame.draw.line(screen, "orange", (370, 429), (370, 479), 3)
    button3 = "Exit"
    button3_surf = button_font.render(button3, True, "white")
    end_rect = button3_surf.get_rect(center=(325, 454))
    screen.blit(button3_surf, end_rect)

def victory_screen():
    button_font = pygame.font.Font(None, 25)
    background_image = pygame.image.load("background_Sudoku.jpg")
    screen.blit(background_image, background_image.get_rect(center=(202.5, 252)))
    victory_text = "Game Won!"
    victory_message = pygame.font.Font(None, 60)
    victory_surf = victory_message.render(victory_text, True, "black")
    victory_rect = victory_surf.get_rect(center=(202.5, 100))
    screen.blit(victory_surf, victory_rect)
    pygame.draw.line(screen, "orange", (280, 454), (370, 454), 3)
    pygame.draw.line(screen, "orange", (280, 454), (280, 504), 3)
    pygame.draw.line(screen, "orange", (280, 504), (370, 504), 3)
    pygame.draw.line(screen, "orange", (370, 454), (370, 504), 3)
    button3 = "Exit"
    button3_surf = button_font.render(button3, True, "white")
    end_rect = button3_surf.get_rect(center=(202.5, 300))
    screen.blit(button3_surf, end_rect)

def loss_screen():
    button_font = pygame.font.Font(None, 25)
    background_image = pygame.image.load("background_Sudoku.jpg")
    screen.blit(background_image, background_image.get_rect(center=(202.5, 252)))
    victory_text = "Game Over :("
    victory_message = pygame.font.Font(None, 60)
    victory_surf = victory_message.render(victory_text, True, "black")
    victory_rect = victory_surf.get_rect(center=(202.5, 100))
    screen.blit(victory_surf, victory_rect)
    pygame.draw.line(screen, "orange", (280, 454), (370, 454), 3)
    pygame.draw.line(screen, "orange", (280, 454), (280, 504), 3)
    pygame.draw.line(screen, "orange", (280, 504), (370, 504), 3)
    pygame.draw.line(screen, "orange", (370, 454), (370, 504), 3)
    button3 = "Restart"
    button3_surf = button_font.render(button3, True, "white")
    end_rect = button3_surf.get_rect(center=(202.5, 300))
    screen.blit(button3_surf, end_rect)

def in_game():
    board_display = Board(405, 405, screen, difficulty)

    row = 9
    col = 9

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = event.pos
                row = y // 45
                col = x // 45
                if 30 < x < 120 and 429 < y < 479:
                    #code to reset board
                    print("reset")
                if 155 < x < 245 and 429 < y < 479:
                    pygame.init()
                    pygame.key.set_repeat(1000, 0)
                    pygame.display.set_caption("Sudoku")
                    opening_Screen()
                    pygame.display.flip()
                    return
                if 280 < x < 370 and 429 < y < 479:
                    print("Game was quit")
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    row -= 1
                if event.key == pygame.K_DOWN:
                    row += 1
                if event.key == pygame.K_RIGHT:
                    col += 1
                if event.key == pygame.K_LEFT:
                    col -= 1

        screen.fill("light blue")
        board_display.draw()
        in_game_screen()

        # Code for select function

        if row > 8:
            row = 8
        if col > 8:
            col = 8
        if row < 0:
            row = 0
        if col < 0:
            col = 0

        board_display.select(row, col)
        pygame.display.flip()

def check_solution(player_board, board_sol):
    print("check_solution")

opening_Screen()
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = pygame.mouse.get_pos()
            difficulty = difficulty_selection(x, y)
            if difficulty == "easy":
                board, board_sol = generate_sudoku(9, 30)
                in_game()
            elif difficulty == "medium":
                board, board_sol = generate_sudoku(9, 40)
                in_game()
            elif difficulty == "hard":
                board, board_sol = generate_sudoku(9, 50)
                in_game()