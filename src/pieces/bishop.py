from pieces.piece import Piece
class Bishop(Piece):
    piece_type="bishop"
    
    def __init__(self, color, grid, move_count=0):
        super().__init__(color, move_count)
        self.grid = grid

    def is_valid_move(self, current_tile, new_tile):
        if not self.__class__.__bases__[0].is_valid_move(self, current_tile, new_tile):
            return False

        if abs(current_tile.x - new_tile.x) == abs(current_tile.y - new_tile.y):
            x_back = -1 if current_tile.x > new_tile.x else 1
            y_back = -1 if current_tile.y > new_tile.y else 1

            for i in range(1, abs(current_tile.x - new_tile.x)):
                if self.grid.tiles[current_tile.x + i*x_back][current_tile.y + i*y_back].piece is not None:
                    return False
            return True
        return False