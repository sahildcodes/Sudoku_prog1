class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.col = col
        self.row = row
        self.screen = screen
        self.sketched_value = ""
        self.selected = False
    
    def set_cell_value(self, value):
        pass
    
    def set_sketched_value(self, value):
        pass
    
    def draw(self):
        pass