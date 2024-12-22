import pygame

CELL_SIZE = 100
GRID_SIZE = 7
SCREEN = WIDTH, HEIGHT = 900, 900
PADDING = (WIDTH - (GRID_SIZE + 1) * CELL_SIZE) / 2
ROWS = COLS = GRID_SIZE
LINE_WIDTH = 7
DOT_RADIUS = 12
DOT_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (240, 240, 240)

def draw_background():
    win.fill(BACKGROUND_COLOR)

def draw_grid():
    for r in range(ROWS):
        for c in range(COLS):
            pygame.draw.circle(win, DOT_COLOR, ((c + 1) * CELL_SIZE + PADDING, (r + 1) * CELL_SIZE + PADDING), DOT_RADIUS)

# draw line between dots
def draw_line(start, end, color):
    pygame.draw.line(win, color, start, end, LINE_WIDTH)

# draw colored dots when it is selected
def draw_circle(r, c, color):
    pygame.draw.circle(win, color, ((c + 1) * CELL_SIZE + PADDING, (r + 1) * CELL_SIZE + PADDING), DOT_RADIUS + 4)

# check if mouse click is inside the dot
def collide_circle(r, c, pos):
    circle_center = ((c + 1) * CELL_SIZE + PADDING, (r + 1) * CELL_SIZE + PADDING)
    circle_radius = DOT_RADIUS + 5

    px, py = pos
    cx, cy = circle_center
    if (px - cx)**2 + (py - cy)**2 <= circle_radius**2:
        return True
    return False


win = pygame.display.set_mode(SCREEN)