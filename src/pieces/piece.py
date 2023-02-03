import pygame
from util.constants import TILE_SIZE
class Piece():
    def __init__(self, color):
        self.color = color

        if self.color == "white":
            path = "static/sprites/chess-pawn-regular.svg"
        else:
            path = "static/sprites/chess-pawn-solid.svg"
        self.image = pygame.image.load(path)
        self.image = pygame.transform.smoothscale(self.image, (TILE_SIZE, TILE_SIZE))
        #self.image = pygame.Surface([40, 40])
    
    def is_valid_move(self, x, y):
        if x < 0 or y < 0:
            return False
        return True