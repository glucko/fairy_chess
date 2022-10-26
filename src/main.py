import pygame
import sys

from util.grid import Grid
from util.tile import Tile
from pieces.piece import Piece

BLACK = (148,83,50)
WHITE = (222,185,145)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    draw_grid()
    grid = init_grid()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        render_pieces(grid)

        pygame.display.update()

def render_pieces(grid):
    tile_size = WINDOW_HEIGHT // 8
    for i in grid.tiles:
        for j in i:
            if j.piece:
                piece = j.piece
                SCREEN.blit(piece.image, piece.rect)

def init_grid():
    tiles = []
    grid = Grid(8, 8)
    for x in range(8):
        tiles.append(Tile(x, 0, Piece(grid, "black", (x, 0))))
        tiles.append(Tile(x, 7, Piece(grid, "white", (x, 7))))
    grid.add_pieces(tiles)
    return grid

def draw_grid():
    blockSize = WINDOW_HEIGHT // 8
    for x in range(0, 8):
        for y in range(0, 8):
            rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            
            if (x + y) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(SCREEN, color, rect)

if __name__ == '__main__':
    main()