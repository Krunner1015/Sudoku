import pygame


BG_COLOR = (173, 216, 230)
pygame.init()
screen = pygame.display.set_mode((720, 720))

def drawLines():
        for i in range(0, 3):
            pygame.draw.line(screen, "black", (0, i * 240), (720, i * 240), 5)
            pygame.draw.line(screen, "black", (i * 240, 0), (i * 240, 720), 5)
            for i in range(0, 9):
                pygame.draw.line(screen, "black", (0, i * 80), (720, i * 80), 2)
            for i in range(0, 9):
                pygame.draw.line(screen, "black", (i * 80, 0), (i * 80, 720), 2)

def opening_Screen():
            background_image = pygame.image.load("background_Soduko.jpg")
            screen.blit(background_image, background_image.get_rect(center =(500, 350)))
            welcome = "Welcome to Sudoku"
            intro = pygame.font.Font(None, 100)
            welcome_surf = intro.render(welcome, 0, "black")
            welcome_rect = welcome_surf.get_rect(center=(375, 200))
            screen.blit(welcome_surf, welcome_rect)
            options = "Select Game Mode"
            options_1 = pygame.font.Font(None, 50)
            options_surf = options_1.render(options, 0, "black")
            options_rect = options_surf.get_rect(center=(375, 400))
            screen.blit(options_surf, options_rect)
            difficulty = pygame.font.Font(None, 40)
            easy_text = "Easy"
            medium_text = "Medium"
            hard_text = "Hard"
            pygame.draw.line(screen, "orange", (80, 480), (240, 480), 3)
            pygame.draw.line(screen, "orange", (80, 480), (80, 560), 3)
            pygame.draw.line(screen, "orange", (80, 560), (240, 560), 3)
            pygame.draw.line(screen, "orange", (240, 480), (240, 560), 3)
            easy_surf = difficulty.render(easy_text, 0, "white")
            end_rect = easy_surf.get_rect(center=(159, 515))
            screen.blit(easy_surf, end_rect)

            pygame.draw.line(screen, "orange", (320, 480), (480, 480), 3)
            pygame.draw.line(screen, "orange", (320, 480), (320, 560), 3)
            pygame.draw.line(screen, "orange", (320, 560), (480, 560), 3)
            pygame.draw.line(screen, "orange", (480, 480), (480, 560), 3)
            medium_surf = difficulty.render(medium_text, 0, "white")
            end_rect = medium_surf.get_rect(center=(401, 515))
            screen.blit(medium_surf, end_rect)

            pygame.draw.line(screen, "orange", (560, 480), (720, 480), 3)
            pygame.draw.line(screen, "orange", (560, 480), (560, 560), 3)
            pygame.draw.line(screen, "orange", (560, 560), (720, 560), 3)
            pygame.draw.line(screen, "orange", (720, 480), (720, 560), 3)
            hard_surf = difficulty.render(hard_text, 0, "white")
            end_rect = hard_surf.get_rect(center=(643, 515))
            screen.blit(hard_surf, end_rect)

screen.fill(BG_COLOR)
drawLines()
difficulty_button()


while True:
    pygame.init()
    screen.fill(BG_COLOR)
    drawLines()
    difficulty_button()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


