from pieces.piece import Piece
class King(Piece):
    piece_type="king"

    def is_valid_move(self, current_tile, new_tile):
        if not super().is_valid_move(current_tile, new_tile):
            return False
        if abs(current_tile.x - new_tile.x) <= 1 and abs(current_tile.y - new_tile.y) <= 1:
            return True
        return False