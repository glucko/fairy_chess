from .tile import Tile

class Grid():
    def __init__(self, width, height, tiles=None):
        self.width = width
        self.height = height
        if tiles is None:
            self.tiles = [[Tile(x, y) for y in range(height)] for x in range(width)]
        else:
            self.tiles = tiles

    def add_pieces(self, new_tiles):
        for tile in new_tiles:
            self.tiles[tile.x][tile.y] = tile
    
    def move_piece(self, current_tile, new_tile):
        if current_tile.piece is None:
            return 0, "No piece on current tile"
        if current_tile.piece.is_valid_move(current_tile, new_tile):
            new_tile.piece = current_tile.piece
            new_tile.piece.move_count += 1
            current_tile.piece = None
            return 1
        return 0, "Invalid move"
    