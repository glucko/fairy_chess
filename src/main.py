import pygame
import sys

from util.grid import Grid
from util.tile import Tile
from util.constants import *
from pieces.piece import Piece
from pieces.pawn import Pawn


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
                if hovered_tile != None and hovered_tile.piece != None:
                    selected_tile = hovered_tile
            if event.type == pygame.MOUSEBUTTONUP:
                drop_tile = get_square_under_mouse(grid)
                if drop_tile and selected_tile:
                    print(grid.move_piece(selected_tile, drop_tile))
                selected_piece = None

        draw_grid()
        render_pieces(grid)

        if hovered_tile != None:
            rect = (BOARD_POS[0] + hovered_tile.x * TILE_SIZE, BOARD_POS[1] + hovered_tile.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(SCREEN, (255, 0, 0, 50), rect, 2)

        pygame.display.flip()

def render_pieces(grid):
    for row in grid.tiles:
        for tile in row:
            if tile.piece:
                SCREEN.blit(tile.piece.image, tile.rect)
                #pygame.draw.rect(SCREEN, (255,0,0), tile.rect)

def init_grid():
    tiles = []
    grid = Grid(8, 8)
    for x in range(8):
        tiles.append(Tile(x, 1, Pawn("white")))
        tiles.append(Tile(x, 6, Pawn("black")))
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
            return grid.tiles[x][y]
    except IndexError: pass
    return None

if __name__ == '__main__':
    main()