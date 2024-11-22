import pygame
import sys

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty


    def draw(self):
        # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        # Draws every cell on this board.
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


        

    def click(self, row, col):
        if 0 <= row < self.height and 0 <= col < self.width:
            row = row // 45
            col = col // 45
            pos = (row, col)
            return pos
        return None


    def clear(self):
    # 	Clears the value cell. 
    # Note that the user can only remove the cell values and 
    # sketched values that are filled by themselves.
        pass

    def sketch(self, value):
        # Sets the sketched value of the current selected cell equal to the user entered value.
        # It will be displayed at the top left corner of the cell using the draw() function.
        pass

    def place_number(self, value):
        # Sets the value of the current selected cell equal to the user entered value. 
        # Called when the user presses the Enter key.
        pass

    def reset_to_original(self):
        # Resets all cells in the board to their original values 
        # (0 if cleared, otherwise the corresponding digit).
        pass

    def is_full(self):
        # Returns a Boolean value indicating whether the board is full or not.
        pass

    def update_board(self):
        # Updates the underlying 2D board with the values in all cells.
        pass

    def find_empty(self):
        # Finds an empty cell and returns its row and col as a tuple (x,y).
        pass

    def check_board(self):
        # Check whether the Sudoku board is solved correctly.
        pass