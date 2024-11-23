import pygame, sys
from sudoku_generator import *
from cell import *
from board import *

BG_COLOR = (173, 216, 230)
game_over = False
board_display = None

pygame.init()
pygame.key.set_repeat(1000,0)
screen = pygame.display.set_mode((405, 504))
pygame.display.set_caption("Sudoku")
font = pygame.font.SysFont("Arial", 30)

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
    difficulty_font = pygame.font.Font(None, 25)
    easy_text = "Easy"
    medium_text = "Medium"
    hard_text = "Hard"
    pygame.draw.line(screen, "orange", (30, 352), (120, 352), 3)
    pygame.draw.line(screen, "orange", (30, 352), (30, 402), 3)
    pygame.draw.line(screen, "orange", (30, 402), (120, 402), 3)
    pygame.draw.line(screen, "orange", (120, 352), (120, 402), 3)
    easy_surf = difficulty_font.render(easy_text, True, "white")
    end_rect = easy_surf.get_rect(center=(75, 377))
    screen.blit(easy_surf, end_rect)

    pygame.draw.line(screen, "orange", (155, 352), (245, 352), 3)
    pygame.draw.line(screen, "orange", (155, 352), (155, 402), 3)
    pygame.draw.line(screen, "orange", (155, 402), (245, 402), 3)
    pygame.draw.line(screen, "orange", (245, 352), (245, 402), 3)
    medium_surf = difficulty_font.render(medium_text, True, "white")
    end_rect = medium_surf.get_rect(center=(200, 377))
    screen.blit(medium_surf, end_rect)

    pygame.draw.line(screen, "orange", (280, 352), (370, 352), 3)
    pygame.draw.line(screen, "orange", (280, 352), (280, 402), 3)
    pygame.draw.line(screen, "orange", (280, 402), (370, 402), 3)
    pygame.draw.line(screen, "orange", (370, 352), (370, 402), 3)
    hard_surf = difficulty_font.render(hard_text, True, "white")
    end_rect = hard_surf.get_rect(center=(325, 377))
    screen.blit(hard_surf, end_rect)

def difficulty_selection(click_x, click_y):
    easy = (30, 352, 120, 402)
    medium = (155, 352, 245, 402)
    hard = (280, 352, 370, 402)

    if easy[0] < click_x < easy[2] and easy[1] < click_y < easy[3]:
        return "Easy"

    if medium[0] < click_x < medium[2] and medium[1] < click_y < medium[3]:
        return "Medium"

    if hard[0] < click_x < hard[2] and hard[1] < click_y < hard[3]:
        return "Hard"

def in_game_buttons():
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

def draw_board(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                continue
            else:
                cell_surf = font.render(str(board[row][col]), True, (0, 0, 0))
                cell_rect = cell_surf.get_rect(topleft=(col * 45 + 42 / 2, row * 45 - 1 / 2))
                screen.blit(cell_surf, cell_rect)

def in_game():
    global board_display
    board_display = Board(405, 405, screen, difficulty)
    pygame.display.set_caption(f"Sudoku - {difficulty}")
    board = [row[:] for row in original_board]
    row = 9
    col = 9
    sketched_number = None
    small_font = pygame.font.SysFont("Arial", 20)
    sketched_board = [[None for _ in range(9)] for _ in range(9)]

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
                    board = [row[:] for row in original_board]
                    print("board reset")
                    screen.fill("light blue")
                    board_display.draw()
                    in_game_buttons()
                    draw_board(board)
                    pygame.display.flip()
                    continue
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
                if event.key in [pygame.K_1, pygame.K_KP1, pygame.K_2, pygame.K_KP2,
                                 pygame.K_3, pygame.K_KP3, pygame.K_4, pygame.K_KP4,
                                 pygame.K_5, pygame.K_KP5, pygame.K_6, pygame.K_KP6,
                                 pygame.K_7, pygame.K_KP7, pygame.K_8, pygame.K_KP8,
                                 pygame.K_9, pygame.K_KP9]:
                    sketched_number = event.key - pygame.K_1 + 1
                    sketched_board[row][col] = sketched_number
                if event.key == pygame.K_RETURN and sketched_board[row][col] is not None:
                    board[row][col] = sketched_board[row][col]
                    sketched_board[row][col] = None

        # Code for select function

        row = max(0, min(8, row))
        col = max(0, min(8, col))

        screen.fill("light blue")
        board_display.draw()
        in_game_buttons()
        draw_board(board)

        for r in range(9):
            for c in range(9):
                if sketched_board[r][c] is not None:
                    sketched_number_surf = small_font.render(str(sketched_board[r][c]), True, (80, 80, 80))
                    sketched_number_rect = sketched_number_surf.get_rect(topleft=(c * 45 + 2, r * 45 + 2))
                    screen.blit(sketched_number_surf, sketched_number_rect)

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
            if difficulty == "Easy":
                board, board_sol = generate_sudoku(9, 30)
                original_board = board
                in_game()
            elif difficulty == "Medium":
                board, board_sol = generate_sudoku(9, 40)
                original_board = board
                in_game()
            elif difficulty == "Hard":
                board, board_sol = generate_sudoku(9, 50)
                original_board = board
                in_game()
