import pygame

class Cell:
    def __init__(self,value,row,col,screen):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
    
    def set_cell_value(self,value):
        self.value = value
    
    def set_sketched_value(self,value):
        self.sketched_value = value
    
    def draw(self):
        font = pygame.font.SysFont("Arial",40)
        if self.value != 0:
            text = font.render(str(self.value),True,(0,0,0))
            self.screen.blit(text, (self.col * 60 +20, self.row * 60 + 10))
        elif self.sketched_value != 0:
            text = font.render(str(self.sketched_value),True,(128,128,128))
            self.screen.blit(text, (self.col * 60 +5, self.row * 60 + 5))
        else:
            pygame.draw.rect(self.screen,(255,0,0), (self.col * 60, self.row * 60,60,60),3)