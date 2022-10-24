class Grid():
    def __init__(self, tiles):
        self.width = width
        self.height = height
        self.tiles = tiles
    
    def move_piece(self, piece, new_tile):
        if piece.is_valid_move(new_tile.x. new_tile.y):
            if new_tile.piece:
                new_tile.piece.kill()
            piece.tile = (x, y, piece)
            return True
        return False
    
    def kill(self, piece):
        piece.tile = (None, None, None)