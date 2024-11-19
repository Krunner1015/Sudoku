chip_font = 400
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        set.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        if 0 < self.value <= 9:
            chip_value = chip_font.render(str(self.value),0,(66,66,66))
            for row in range(9):
                for col in range(9):
                    chip_value.get_rect(center = (col * 80 + 40, row * 80 + 40))
##flag run = - 