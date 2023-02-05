from pieces.piece import Piece
class Pawn(Piece):
    piece_type="pawn"

    def is_valid_move(self, current_tile, new_tile):
        if not super().is_valid_move(current_tile, new_tile):
            return False
        if current_tile.piece.color == "white":
            if current_tile.x == new_tile.x and new_tile.piece is None:
                if self.move_count == 0 and current_tile.y == new_tile.y - 2:
                    return True
                if current_tile.y == new_tile.y - 1:
                    return True
            else:
                if abs(current_tile.x - new_tile.x) == 1 and current_tile.y == new_tile.y - 1 and new_tile.piece is not None:
                    return True
        else:
            if current_tile.x == new_tile.x and new_tile.piece is None:
                if self.move_count == 0 and current_tile.y == new_tile.y + 2:
                    return True
                if current_tile.y == new_tile.y + 1:
                    return True
            else:
                if abs(current_tile.x - new_tile.x) == 1 and current_tile.y == new_tile.y + 1 and new_tile.piece is not None:
                    return True
        return False