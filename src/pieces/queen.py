from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.piece import Piece
class Queen(Piece):
    piece_type="queen"

    def __init__(self, color, grid, move_count=0):
        super().__init__(color, move_count)
        self.grid = grid

    def is_valid_move(self, current_tile, new_tile):
        if Rook.is_valid_move(self, current_tile, new_tile) or Bishop.is_valid_move(self, current_tile, new_tile):
            return True
