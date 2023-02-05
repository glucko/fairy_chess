import pygame
from util.constants import TILE_SIZE
class Piece():
    piece_type="pawn"
    def __init__(self, color, type="pawn", move_count=0):
        self.color = color
        self.move_count = 0

        if self.color == "white":
            path = f"static/sprites/chess-{self.piece_type}-regular.svg"
        else:
            path = f"static/sprites/chess-{self.piece_type}-solid.svg"
        self.image = pygame.image.load(path)
        self.image = pygame.transform.smoothscale(self.image, (TILE_SIZE, TILE_SIZE))
        #self.image = pygame.Surface([40, 40])
    
    def is_valid_move(self, current_tile, new_tile):
        if 7 < new_tile.x < 0 or 7 < new_tile.y < 0:
            return False
        if current_tile.x == new_tile.x and current_tile.y == new_tile.y:
            return False
        return True