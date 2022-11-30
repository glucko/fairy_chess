import pygame
import sys

from util.grid import Grid
from util.tile import Tile
from pieces.piece import Piece

BLACK = (148,83,50)
WHITE = (222,185,145)
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
TILE_SIZE = WINDOW_HEIGHT // 8
BOARD_POS = (0, 0)


def main():
    pygame.init()

    global SCREEN, CLOCK
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()

    SCREEN.fill(BLACK)

    grid = init_grid()

    selected_tile = None
    while True:
        hovered_tile = get_square_under_mouse(grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hovered_tile != None:
                    selected_tile = hovered_tile
            if event.type == pygame.MOUSEBUTTONUP:
                drop_tile = get_square_under_mouse(grid)
                if drop_tile:
                    drop_tile.piece = selected_tile.piece
                    selected_tile.piece = None
                selected_piece = None
                drop_pos = None
                    

        draw_grid()
        render_pieces(grid)

        if hovered_tile.x != None:
            rect = (BOARD_POS[0] + hovered_tile.x * TILE_SIZE, BOARD_POS[1] + hovered_tile.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(SCREEN, (255, 0, 0, 50), rect, 2)

        pygame.display.flip()

def render_pieces(grid):
    for i in grid.tiles:
        for j in i:
            if j.piece:
                piece = j.piece
                SCREEN.blit(piece.image, piece.rect)

def init_grid():
    tiles = []
    grid = Grid(8, 8)
    for x in range(8):
        tiles.append(Tile(0, x, Piece(grid, "black", (x, 0))))
        tiles.append(Tile(7, x, Piece(grid, "white", (x, 7))))
    grid.add_pieces(tiles)
    return grid

def draw_grid():
    for x in range(0, 8):
        for y in range(0, 8):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            
            if (x + y) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(SCREEN, color, rect)

def get_square_under_mouse(grid):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) - BOARD_POS
    x, y = [int(v // TILE_SIZE) for v in mouse_pos]
    try: 
        if x >= 0 and y >= 0:
            return Tile(x, y, grid.tiles[y][x].piece)
    except IndexError: pass
    return None

if __name__ == '__main__':
    main()