import pygame
import sys
import pygame_gui

from grid import Grid
from tile import Tile
from constants import *
from pieces.piece import Piece
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.king import King
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.knight import Knight

def main():
    pygame.init()

    global SCREEN, CLOCK
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()

    SCREEN.fill(BLACK)

    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#000000'))

    layout_rect = pygame_gui.elements.UIWindow(pygame.Rect(10, 10, 200, 560))

    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 5), (100, 50)),
                                                text='Start',
                                                manager=manager,
                                                container=layout_rect)
    stop_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 5+50), (100, 50)),
                                                text='Stop',
                                                manager=manager,
                                                container=layout_rect)
    grid = init_grid()

    app_running = True
    run_game = False

    selected_tile = None
    turn = 'white'
    while app_running:
        SCREEN.blit(background, (0, 0))
        time_delta = CLOCK.tick(60)/1000.0
        hovered_tile = get_square_under_mouse(grid)
        selected_tile = None

        # !!!!!!!!! EVENTS !!!!!!!!!
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app_running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    run_game = True
                if event.ui_element == stop_button:
                    run_game = False
            if run_game:
                game_events(event, grid, hovered_tile, selected_tile, turn)
            manager.process_events(event)

        if run_game: 
            render_grid()
            render_pieces(grid)

            if hovered_tile != None:
                rect = (BOARD_POS[0] + hovered_tile.x * TILE_SIZE, BOARD_POS[1] + hovered_tile.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(SCREEN, (255, 0, 0, 50), rect, 2)
                
        manager.draw_ui(SCREEN)
        manager.update(time_delta)
        pygame.display.flip()

def game_events(event, grid, hovered_tile, selected_tile, turn):
    print("sussy")
    if event.type == pygame.MOUSEBUTTONDOWN:
        if hovered_tile != None and hovered_tile.piece != None and hovered_tile.piece.color == turn:
            selected_tile = hovered_tile
    if event.type == pygame.MOUSEBUTTONUP:
        drop_tile = get_square_under_mouse(grid)
        if drop_tile and selected_tile:
            outcome = grid.move_piece(selected_tile, drop_tile)
            if outcome == 2:
                print(f"{turn} wins!")
            if outcome == 1:
                turn = 'black' if turn == 'white' else 'white'
            print(turn)

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

    # adds rooks
    tiles.append(Tile(0, 0, Rook("white", grid)))
    tiles.append(Tile(7, 0, Rook("white", grid)))
    tiles.append(Tile(0, 7, Rook("black", grid)))
    tiles.append(Tile(7, 7, Rook("black", grid)))

    # adds bishops
    tiles.append(Tile(2, 0, Bishop("white", grid)))
    tiles.append(Tile(5, 0, Bishop("white", grid)))
    tiles.append(Tile(2, 7, Bishop("black", grid)))
    tiles.append(Tile(5, 7, Bishop("black", grid)))

    # adds knights
    tiles.append(Tile(1, 0, Knight("white", grid)))
    tiles.append(Tile(6, 0, Knight("white", grid)))
    tiles.append(Tile(1, 7, Knight("black", grid)))
    tiles.append(Tile(6, 7, Knight("black", grid)))

    # adds queens
    tiles.append(Tile(3, 0, Queen("white", grid)))
    tiles.append(Tile(3, 7, Queen("black", grid)))

    # adds kings
    tiles.append(Tile(4, 0, King("white", grid)))
    tiles.append(Tile(4, 7, King("black", grid)))
    
    grid.add_pieces(tiles)
    return grid

def render_grid():
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