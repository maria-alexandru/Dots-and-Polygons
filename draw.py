import pygame

SCREEN = WIDTH, HEIGHT = 1000, 1000
CELLSIZE = 100
PADDING = 50
ROWS = COLS = 8 # (WIDTH - 4 * PADDING) // CELLSIZE
print(ROWS, COLS)

pygame.init()
win = pygame.display.set_mode(SCREEN)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for r in range(ROWS):
        for c in range(COLS):
            pygame.draw.circle(win, (255, 255, 255), (c * CELLSIZE + 3 * PADDING, r * CELLSIZE + 3 * PADDING), 10)
    pygame.display.update()

pygame.quit()