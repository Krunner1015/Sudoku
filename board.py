import pygame
from sudoku_generator import SudokuGenerator
import sys

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.select_x = 0
        self.select_y = 0


    def draw(self):
        # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        for i in range(0, 4):
                pygame.draw.line(self.screen, "black", (0, i * 135), (405, i * 135), 4)
                pygame.draw.line(self.screen, "black", (i * 135, 0), (i * 135, 405), 4)
                for i in range(0, 9):
                    pygame.draw.line(self.screen, "black", (0, i * 45), (405, i * 45), 2)
                for i in range(0, 9):
                    pygame.draw.line(self.screen, "black", (i * 45, 0), (i * 45, 405), 2)


    def select(self, row, col):
        # Marks the cell at (row, col) in the board as the current selected cell.
        # Once a cell has been selected, the user can edit its value or sketched value.
        pygame.draw.rect(self.screen, "red", pygame.Rect(col*self.width/9, row*self.height/9, 2, 47))
        pygame.draw.rect(self.screen, "red", pygame.Rect(col*self.width/9, row*self.height/9, 47,2))
        pygame.draw.rect(self.screen, "red", pygame.Rect(self.width/9+col*self.width/9, row*self.height/9, 2, 47))
        pygame.draw.rect(self.screen, "red", pygame.Rect(col*self.width/9, self.height/9+row*self.height/9, 47,2))
        self.select_x = row
        self.select_y = col