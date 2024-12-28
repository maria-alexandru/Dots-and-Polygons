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
LINE_WIDTH = 8
DOT_RADIUS = 8
DOT_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (240, 240, 240)

screen = screen_width, screen_height
padding_width = (screen_width - (grid_size + 1) * cell_size) / 2
padding_height = (screen_height - (grid_size + 1) * cell_size) / 2

lines = []
selected_points = []

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


#verify if there is a dot between lines
def is_point_inside_cell(point, cell):
    return cell.rect.collide_circle(point)

# draw line between dots
def draw_line(start, end, color, cells):
    global lines

    # normalize points
    line = tuple(sorted((start, end)))

    if line not in lines:
        pygame.draw.line(win, color, start, end, LINE_WIDTH)
        lines.append(line)
        
        for cell in cells:
                #horizontal
                if start[1] == end[1]:
                    if start[0] < end[0]:
                        cell.sides[0] = True
                    else:
                        cell.sides[2] = True
                elif start[0] == end[0]: #vertical
                    if start[1] < end[1]:
                        cell.sides[3] = True
                    else:
                        cell.sides[1] = True
                else:
                    if start[0] < end[0]:
                        cell.sides[4] = True
                    else:
                        cell.sides[5] = True

        return True
    return False

# check if two points are adjacent
def is_adjacent(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    # horizontal adjacency
    if abs(x1-x2) == cell_size and y1 == y2:
        return True

    if abs(y1 - y2) == cell_size and x1 == x2:
        return True

    if abs(x1 - x2) == cell_size and abs(y1 - y2) == cell_size:
        return True
    return False

# verify if the dot is connected to a line
def is_connected(point):
    for line in lines:
        if point in line:
            return True
    return False

#select two dots and draw the line
def select_point(r, c, pos, cells):
    global selected_points
    circle_center = ((c + 1) * cell_size + padding_width, (r + 1) * cell_size + padding_height)
    if collide_circle(r, c, pos):
        selected_points.append(circle_center)

        #try to draw the line
        if len(selected_points) == 2:
            if is_adjacent(selected_points[0], selected_points[1]):    
                draw_line(selected_points[0], selected_points[1], (130, 208, 209), cells)
                
                for point in selected_points:
                    pygame.draw.circle(win, (130, 109, 168), point, DOT_RADIUS + 4)
            #reset selection
            selected_points = []

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