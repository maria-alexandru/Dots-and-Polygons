import ctypes
import pygame

pygame.init()
info = pygame.display.Info()

# # get the screen resolution (width and height)
# screen_width = info.current_w
# screen_height = info.current_h

# Screen settings
screen_width, screen_height = 1280, 720
win = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Dots and Polygons Menu")

grid_size = 8
cell_size = min(screen_height / (grid_size + 1), screen_width / (grid_size + 1))

rows = cols = grid_size
LINE_WIDTH = 4
DOT_RADIUS = 8
DOT_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (240, 240, 240)

screen = screen_width, screen_height
padding_width = (screen_width - (grid_size + 1) * cell_size) / 2
padding_height = (screen_height - (grid_size + 1) * cell_size) / 2

def get_size():
    global screen_width, screen_height, info, padding_height, padding_width, cell_size

    # get the screen resolution (width and height)
    info = pygame.display.Info()
    screen_width = info.current_w
    screen_height = info.current_h
    cell_size = min(screen_height / (grid_size + 1), screen_width / (grid_size + 1))
    padding_width = (screen_width - (grid_size + 1) * cell_size) / 2
    padding_height = (screen_height - (grid_size + 1) * cell_size) / 2

def draw_background():
    win.fill(BACKGROUND_COLOR)

def draw_grid():
    get_size()
    draw_background()

    for r in range(rows):
        for c in range(cols):
            pygame.draw.circle(win, DOT_COLOR, ((c + 1) * cell_size + padding_width, (r + 1) * cell_size + padding_height), DOT_RADIUS)

# draw line between dots
def draw_line(start, end, color):
    pygame.draw.line(win, color, start, end, LINE_WIDTH)

# draw colored dots when it is selected
def draw_circle(r, c, color):
    pygame.draw.circle(win, color, ((c + 1) * cell_size + padding_width, (r + 1) * cell_size + padding_height), DOT_RADIUS + 4)

# check if mouse click is inside the dot
def collide_circle(r, c, pos):
    circle_center = ((c + 1) * cell_size + padding_width, (r + 1) * cell_size + padding_height)
    circle_radius = DOT_RADIUS + 5

    px, py = pos
    cx, cy = circle_center
    if (px - cx)**2 + (py - cy)**2 <= circle_radius**2:
        return True
    return False
