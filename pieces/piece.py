import pygame
class Piece():
    def __init__(self, grid, color, coords):
        self.grid = grid
        self.color = color
        self.x, self.y = coords

        self.rect = pygame.Rect(self.x*40, self.y*40, 16, 16)
        self.image = pygame.image.load("static\sprites\pawn.png")
    
    def is_valid_move(self, x, y):
        if x < 0 or y < 0:
            return False
        return True