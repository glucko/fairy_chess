from pieces.piece import Piece
class Rook(Piece):
    piece_type="rook"

    def __init__(self, color, grid, type="rook", move_count=0):
        super().__init__(color, type, move_count)
        self.grid = grid

    def is_valid_move(self, current_tile, new_tile):
        if not super().is_valid_move(current_tile, new_tile):
            return False
            
        if current_tile.x == new_tile.x:
            back = -1 if current_tile.y > new_tile.y else 1

            for i in range(current_tile.y+back, new_tile.y, back):
                if self.grid.tiles[current_tile.x][i].piece is not None:
                    return False
            return True

        elif current_tile.y == new_tile.y:
            back = -1 if current_tile.x > new_tile.x else 1

            for i in range(current_tile.x+back, new_tile.x, back):
                if self.grid.tiles[i][current_tile.y].piece is not None:
                    return False
            return True
        return False