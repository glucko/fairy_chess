class Base():
    def __init__(self, coords, grid):
        self.tile = (*coords, self)
        self.grid = grid
    
    def is_valid_move(self, x, y):
        if x < 0 or y < 0:
            return False
        return True