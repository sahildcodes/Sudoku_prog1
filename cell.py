class Cell:
    def __init__(self, value, row, col, is_editable, screen):
        self.value = value
        self.col = col
        self.row = row
        self.screen = screen
        self.is_editable = is_editable
        self.sketched_value = ""
        self.selected = False
    
    def set_cell_value(self, value):
        self.value = value
    
    def set_sketched_value(self, value):
        self.sketched_value = value
        
    def set_selected(self, value):
        self.selected = value
        
    def set_is_editable(self, value):
        self.is_editable = value
        
    def get_is_editable(self, value):
        return self.is_editable
    
    """
    Eventually, this will probably have to hook into pygame. For now, I am 
    just going to have it print the cell's current value inside brackets '[]'.
    It will also print the row/col values, sketched value, selected value, and is editable value.
    This is primarily just for debugging purposes right now.
    """
    def draw(self):
        print(f"[{self.value}]")
        print(f"Sketched Value: {self.sketched_value}")
        print(f"Selected Value: {self.selected}")
        print(f"Row, Col: ({self.row}, {self.col})")
        print(f"Is Editable: {self.is_editable}")