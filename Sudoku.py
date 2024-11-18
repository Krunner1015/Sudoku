import pygame
BG_COLOR = (173, 216, 230)
screen = pygame.display.set_mode((405, 504))
pygame.display.set_caption("Sudoku")


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


try:
    pygame.init()
    screen = pygame.display.set_mode((405, 504))
    while True:
        screen.fill("light blue")
        drawLines()
        opening_Screen()
        pygame.display.flip()
finally:
    pygame.quit()

