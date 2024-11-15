import pygame

SCREEN = WIDTH, HEIGHT = 500, 500
CELLSIZE = 50
PADDING = 80
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
            pygame.draw.circle(win, (255, 255, 255), (c * CELLSIZE + PADDING, r * CELLSIZE + PADDING), 10)
    pygame.display.update()

pygame.quit()