class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.col = col
        self.row = row
        self.screen = screen
        self.sketched_value = ""
        self.selected = False
    
    def set_cell_value(self, value):
        self.value = value
    
    def set_sketched_value(self, value):
        self.sketched_value = value
        
    def set_selected(self, value):
        self.selected = value
    
    def draw(self):
        pass