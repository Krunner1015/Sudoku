import pygame
from pygame import MOUSEBUTTONDOWN

screen = pygame.display.set_mode((405, 504))

def drawLines():
        for i in range(0, 4):
            pygame.draw.line(screen, "black", (0, i * 135), (405, i * 135), 5)
            pygame.draw.line(screen, "black", (i * 135, 0), (i * 135, 405), 5)
            for i in range(0, 9):
                pygame.draw.line(screen, "black", (0, i * 45), (405, i * 45), 2)
            for i in range(0, 9):
                pygame.draw.line(screen, "black", (i * 45, 0), (i * 45, 405), 2)

def opening_Screen():
            background_image = pygame.image.load("background_Soduko.jpg")
            screen.blit(background_image, background_image.get_rect(center =(202.5, 252)))
            welcome = "Welcome to Sudoku"
            intro = pygame.font.Font(None, 60)
            welcome_surf = intro.render(welcome, 0, "black")
            welcome_rect = welcome_surf.get_rect(center=(202.5, 100))
            screen.blit(welcome_surf, welcome_rect)
            options = "Select Game Mode"
            options_1 = pygame.font.Font(None, 40)
            options_surf = options_1.render(options, 0, "black")
            options_rect = options_surf.get_rect(center=(202.5, 175))
            screen.blit(options_surf, options_rect)
            difficulty = pygame.font.Font(None, 25)
            easy_text = "Easy"
            medium_text = "Medium"
            hard_text = "Hard"
            pygame.draw.line(screen, "orange", (30, 352), (120, 352), 3)
            pygame.draw.line(screen, "orange", (30, 352), (30, 402), 3)
            pygame.draw.line(screen, "orange", (30, 402), (120, 402), 3)
            pygame.draw.line(screen, "orange", (120, 352), (120, 402), 3)
            easy_surf = difficulty.render(easy_text, 0, "white")
            end_rect = easy_surf.get_rect(center=(75, 377))
            screen.blit(easy_surf, end_rect)

            pygame.draw.line(screen, "orange", (155, 352), (245, 352), 3)
            pygame.draw.line(screen, "orange", (155, 352), (155, 402), 3)
            pygame.draw.line(screen, "orange", (155, 402), (245, 402), 3)
            pygame.draw.line(screen, "orange", (245, 352), (245, 402), 3)
            medium_surf = difficulty.render(medium_text, 0, "white")
            end_rect = medium_surf.get_rect(center=(200, 377))
            screen.blit(medium_surf, end_rect)

            pygame.draw.line(screen, "orange", (280, 352), (370, 352), 3)
            pygame.draw.line(screen, "orange", (280, 352), (280, 402), 3)
            pygame.draw.line(screen, "orange", (280, 402), (370, 402), 3)
            pygame.draw.line(screen, "orange", (370, 352), (370, 402), 3)
            hard_surf = difficulty.render(hard_text, 0, "white")
            end_rect = hard_surf.get_rect(center=(325, 377))
            screen.blit(hard_surf, end_rect)

def in_game():
    button_font = pygame.font.Font(None, 25)

    pygame.draw.line(screen, "orange", (30, 454), (120, 454), 3)
    pygame.draw.line(screen, "orange", (30, 454), (30, 504), 3)
    pygame.draw.line(screen, "orange", (30, 504), (120, 504), 3)
    pygame.draw.line(screen, "orange", (120, 454), (120, 504), 3)
    button1 = "Reset"
    button1_surf = button_font.render(button1, 0, "white")
    end_rect = button1_surf.get_rect(center=(75, 479))
    screen.blit(button1_surf, end_rect)

    pygame.draw.line(screen, "orange", (155, 454), (245, 454), 3)
    pygame.draw.line(screen, "orange", (155, 454), (155, 504), 3)
    pygame.draw.line(screen, "orange", (155, 504), (245, 504), 3)
    pygame.draw.line(screen, "orange", (245, 454), (245, 504), 3)
    button2 = "Restart"
    button2_surf = button_font.render(button2, 0, "white")
    end_rect = button2_surf.get_rect(center=(200, 479))
    screen.blit(button2_surf, end_rect)

    pygame.draw.line(screen, "orange", (280, 454), (370, 454), 3)
    pygame.draw.line(screen, "orange", (280, 454), (280, 504), 3)
    pygame.draw.line(screen, "orange", (280, 504), (370, 504), 3)
    pygame.draw.line(screen, "orange", (370, 454), (370, 504), 3)
    button3 = "Exit"
    button3_surf = button_font.render(button3, 0, "white")
    end_rect = button3_surf.get_rect(center=(325, 479))
    screen.blit(button3_surf, end_rect)

def victory_screen():
    button_font = pygame.font.Font(None, 25)
    background_image = pygame.image.load("background_Soduko.jpg")
    screen.blit(background_image, background_image.get_rect(center=(202.5, 252)))
    victory_text = "Game Won!"
    victory_message = pygame.font.Font(None, 60)
    victory_surf = victory_message.render(victory_text, 0, "black")
    victory_rect = victory_surf.get_rect(center=(202.5, 100))
    screen.blit(victory_surf, victory_rect)
    pygame.draw.line(screen, "orange", (280, 454), (370, 454), 3)
    pygame.draw.line(screen, "orange", (280, 454), (280, 504), 3)
    pygame.draw.line(screen, "orange", (280, 504), (370, 504), 3)
    pygame.draw.line(screen, "orange", (370, 454), (370, 504), 3)
    button3 = "Exit"
    button3_surf = button_font.render(button3, 0, "white")
    end_rect = button3_surf.get_rect(center=(202.5, 300))
    screen.blit(button3_surf, end_rect)

def loss_screen():
    button_font = pygame.font.Font(None, 25)
    background_image = pygame.image.load("background_Soduko.jpg")
    screen.blit(background_image, background_image.get_rect(center=(202.5, 252)))
    victory_text = "Game Over :("
    victory_message = pygame.font.Font(None, 60)
    victory_surf = victory_message.render(victory_text, 0, "black")
    victory_rect = victory_surf.get_rect(center=(202.5, 100))
    screen.blit(victory_surf, victory_rect)
    pygame.draw.line(screen, "orange", (280, 454), (370, 454), 3)
    pygame.draw.line(screen, "orange", (280, 454), (280, 504), 3)
    pygame.draw.line(screen, "orange", (280, 504), (370, 504), 3)
    pygame.draw.line(screen, "orange", (370, 454), (370, 504), 3)
    button3 = "Restart"
    button3_surf = button_font.render(button3, 0, "white")
    end_rect = button3_surf.get_rect(center=(202.5, 300))
    screen.blit(button3_surf, end_rect)


try:
    pygame.init()
    screen = pygame.display.set_mode((405, 504))
    num_spaces = -1
    while True:
        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.pos[0] in range(30, 121)) and (event.pos[1] in range(352, 403)):
                clicked = True
                break

            elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.pos[0] in range(155, 245)) and (event.pos[1] in range(352, 403)):
                clicked = True
                break

            elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.pos[0] in range(280, 370)) and (event.pos[1] in range(352, 403)):
                clicked = True
                break
        if clicked:
            break

        opening_Screen()
        pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.pos[0] in range(280, 370)) and (event.pos[1] in range(454, 504)):
                pygame.quit()

        screen.fill("light blue")
        drawLines()
        in_game()
        pygame.display.flip()
finally:
    pygame.quit()

