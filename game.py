import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def drawGrid():
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