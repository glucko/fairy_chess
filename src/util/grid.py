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
    
    def move_piece(self, old_tile, new_tile):
        if old_tile.piece.is_valid_move(new_tile.x, new_tile.y):
            new_tile.piece = old_tile.piece
            old_tile.piece = None
            return True
        return False
    