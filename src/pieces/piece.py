import pygame
class Piece():
    def __init__(self, grid, color, coords):
        self.grid = grid
        self.color = color
        self.x, self.y = coords

        piece_size = 40
        tile_size = 50
        multiplier = 2 * piece_size // 10
        
        self.rect = pygame.Rect(
            self.x*tile_size+piece_size//multiplier,
            self.y*tile_size+piece_size//multiplier,
            piece_size,
            piece_size
            )

        self.image = pygame.image.load(f"static/sprites/pawn_{self.color}.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        # self.image = pygame.Surface([40, 40])
        # self.image.fill(color)
    
    def is_valid_move(self, x, y):
        if x < 0 or y < 0:
            return False
        return True