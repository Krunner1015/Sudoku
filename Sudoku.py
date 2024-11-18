import pygame


BG_COLOR = (173, 216, 230)
pygame.init()
screen = pygame.display.set_mode((720, 720))

def drawLines():
    for i in range(0,3):
        for i in range(0, 3):
            pygame.draw.line(screen, "black", (0, i * 80), (720, i * 80), 2)
        for i in range(0, 3):
            pygame.draw.line(screen, "black", (i * 80, 0), (i * 80, 720), 2)
        pygame.draw.line(screen, "black", (0, i * 240), (720, i * 240), 5)
        pygame.draw.line(screen, "black", (i*240, 0), (i*240, 720), 5)

screen.fill(BG_COLOR)
drawLines()

while True:
    pygame.init()
