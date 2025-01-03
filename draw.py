import ctypes
import pygame
import game_manager
# import detect_surface
import math

pygame.init()
info = pygame.display.Info()

# # get the screen resolution (width and height)
# screen_width = info.current_w
# screen_height = info.current_h

# Screen settings
screen_width, screen_height = 1280, 720
win = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Dots and Polygons Menu")

LINE_WIDTH = 8
DOT_RADIUS = 8
DOT_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (240, 240, 240)


# grid_size = 7
# rows = cols = grid_size - 1
# cell_size = min(screen_height / (grid_size + 1), screen_width / (grid_size + 1))
# screen = screen_width, screen_height
# padding_width = (screen_width - (grid_size + 1) * cell_size) / 2
# padding_height = (screen_height - (grid_size + 1) * cell_size) / 2


def init(size):
    global grid_size, padding_height, padding_width, screen, rows, cols, cell_size
    grid_size = size
    rows = cols = grid_size - 1
    cell_size = min(screen_height / (grid_size + 1), screen_width / (grid_size + 1))
    screen = screen_width, screen_height
    padding_width = (screen_width - (grid_size + 1) * cell_size) / 2
    padding_height = (screen_height - (grid_size + 1) * cell_size) / 2

lines = []
selected_points = []
connected_points = []

def get_size(cells):
    global screen_width, screen_height, info, padding_height, padding_width, cell_size

    # get the screen resolution (width and height)
    info = pygame.display.Info()
    # update_points()
    screen_width = info.current_w
    screen_height = info.current_h
    cell_size = min(screen_height / (grid_size + 1), screen_width / (grid_size + 1))
    padding_width = (screen_width - (grid_size + 1) * cell_size) / 2
    padding_height = (screen_height - (grid_size + 1) * cell_size) / 2

    for cell in cells:
        cell.update_dim( cell_size, padding_width, padding_height)

def update_points():
    global selected_points
    print("*************selected points: " + str(selected_points))
    info = pygame.display.Info()
    updated_points = [(math.floor(x * screen_width / info.current_w), math.floor(y * screen_height / info.current_h)) for x, y in selected_points]
    # print(updated_points)
    selected_points = updated_points


def draw_background():
    win.fill(BACKGROUND_COLOR)

def draw_grid(cells):
    get_size(cells)
    draw_background()
    # pygame.display.flip()

    # for r in range(rows):
    #     for c in range(cols):
    #         pygame.draw.circle(win, DOT_COLOR, ((c + 1) * cell_size + padding_width, (r + 1) * cell_size + padding_height), DOT_RADIUS)
    
    # print("////////////////////")
    for index, cell in enumerate(cells):
        pygame.draw.circle(win, DOT_COLOR, cell.rect.topleft, DOT_RADIUS)
        pygame.draw.circle(win, DOT_COLOR, cell.rect.topright, DOT_RADIUS)
        pygame.draw.circle(win, DOT_COLOR, cell.rect.bottomright, DOT_RADIUS)
        pygame.draw.circle(win, DOT_COLOR, cell.rect.bottomleft, DOT_RADIUS)
        # print("--------------")
        # print("rect idx" + str(index)+ str(cell.rect))
        # print("0 - 1 (nr 0)" + str(cell.dots[0]) + " " + str(cell.dots[1])+ " " + str(cell.sides[0]))
        # print("1 - 2 (nr 1)" + str(cell.dots[1]) + " " + str(cell.dots[2])+ " " + str(cell.sides[1]))
        # print("2 - 3 (nr 2)" + str(cell.dots[2]) + " " + str(cell.dots[3])+ " " + str(cell.sides[2]))
        # print("3 - 0 (nr 3)" + str(cell.dots[3]) + " " + str(cell.dots[0])+ " " + str(cell.sides[3]))
        # print("--------------")

        detect_and_color_surface(cells, game_manager.GameManager().selected_mode)
        for index, side in enumerate(cell.sides):
            if side == True:
                draw_line(cell.edges[index][0],  cell.edges[index][1], (130, 208, 209), cells)

        for index, dot in enumerate(cell.dots):
            if dot == True:
                draw_circle(cell.points[index][0], cell.points[index][1], (130, 109, 168))

    # print("////////////////////")

    pygame.display.update()




def detect_and_color_surface(cells, mode):
    for cell in cells:
        # detect complete square
        if mode in ["Square", "Mix"] and cell.is_square_complete():
            print("rect");
            pygame.draw.rect(win, (0, 255, 0), cell.rect)
            draw_line(cell.rect.topleft, cell.rect.topright, (130, 208, 209), cells)
            draw_line(cell.rect.topright, cell.rect.bottomright, (130, 208, 209), cells)
            draw_line(cell.rect.bottomright, cell.rect.bottomleft, (130, 208, 209), cells)
            draw_line(cell.rect.bottomleft, cell.rect.topleft, (130, 208, 209), cells)
            
            pygame.draw.circle(win, (130, 109, 168), cell.rect.topright, DOT_RADIUS + 4)
            pygame.draw.circle(win, (130, 109, 168), cell.rect.topleft, DOT_RADIUS + 4)
            pygame.draw.circle(win, (130, 109, 168), cell.rect.bottomleft, DOT_RADIUS + 4)
            pygame.draw.circle(win, (130, 109, 168), cell.rect.bottomright, DOT_RADIUS + 4)
            
            cell.winner = "Player"

        if mode in ["Triangle", "Mix"] and cell.is_triangle_complete():

            if cell.sides[0] and cell.sides[3] and cell.sides[4]:
                triangle_points = [cell.rect.topleft, cell.rect.topright, cell.rect.bottomleft]
                pygame.draw.polygon(win, (255, 0, 0), triangle_points)
                draw_line(cell.rect.topleft, cell.rect.topright, (130, 208, 209), cells)
                draw_line(cell.rect.topleft, cell.rect.bottomleft, (130, 208, 209), cells)
                draw_line(cell.rect.topright, cell.rect.bottomleft, (130, 208, 209), cells)
                
                pygame.draw.circle(win, (130, 109, 168), cell.rect.topright, DOT_RADIUS + 4)
                pygame.draw.circle(win, (130, 109, 168), cell.rect.topleft, DOT_RADIUS + 4)
                pygame.draw.circle(win, (130, 109, 168), cell.rect.bottomleft, DOT_RADIUS + 4)

            elif cell.sides[2] and cell.sides[1] and cell.sides[5]:
                triangle_points = [cell.rect.topright, cell.rect.bottomright, cell.rect.bottomleft]
                pygame.draw.polygon(win, (255, 0, 0), triangle_points)
                draw_line(cell.rect.topright, cell.rect.bottomright, (130, 208, 209), cells)
                draw_line(cell.rect.topright, cell.rect.bottomleft, (130, 208, 209), cells)
                draw_line(cell.rect.bottomleft, cell.rect.bottomright, (130, 208, 209), cells)

                pygame.draw.circle(win, (130, 109, 168), cell.rect.topright, DOT_RADIUS + 4)
                pygame.draw.circle(win, (130, 109, 168), cell.rect.bottomleft, DOT_RADIUS + 4)
                pygame.draw.circle(win, (130, 109, 168), cell.rect.bottomright, DOT_RADIUS + 4)

            else:
                continue

            cell.winner = "Player"


# verify if there is a dot between lines
def is_point_inside_cell(point, cell):
    return cell.rect.collide_circle(point)

# draw line between dots
def draw_line(start, end, color, cells):
    global lines
    pygame.draw.line(win, color, start, end, LINE_WIDTH)
    pygame.draw.circle(win, (130, 109, 168), start, DOT_RADIUS + 4)
    pygame.draw.circle(win, (130, 109, 168), end, DOT_RADIUS + 4)


    # # normalize points
    # line = tuple(sorted((start, end)))

    # if line not in lines:
    #     lines.append(line)

        # if start not in connected_points:
        #     connected_points.append(start)
        # if end not in connected_points:
        #     connected_points.append(end)

        
        # for cell in cells:
        #     for edge_index, edge in enumerate(cell.edges):
        #         if line == edge:
        #             cell.sides[edge_index] = True

    #     return True
    # return False

# check if two points are adjacent
def is_adjacent(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    # horizontal adjacency
    if abs(abs(x1-x2) - cell_size) <= 1 and abs(y1 - y2) <= 1:
        return True

    if abs(abs(y1 - y2) - cell_size) <= 1 and abs(x1 - x2) <= 1:
        return True

    print(str(x1) + " " + str(x2) + " " + str(cell_size))
    if abs(abs(x1 - x2) - cell_size) <= cell_size and abs(abs(y1 - y2) - cell_size) <= cell_size:
        return True
    return False

# verify if the dot is connected to a line
def is_connected(point):
    for line in lines:
        if point in line:
            return True
    return False

# select two dots and draw the line
def select_point(cell, pos):
    global selected_points
    # circle_center = (math.floor((cell.c + 1) * cell_size + padding_width), math.floor((cell.r + 1) * cell_size + padding_height))
    collide, index = collide_circle(cell, pos)
    if collide:
        # selected_points.append(circle_center)
        if cell.points[index] not in selected_points:
            selected_points.append(cell.points[index])
            print(selected_points)

def try_draw_line(cells):
    global selected_points
    # try to draw the line
    if len(selected_points) >= 2:
        # print(selected_points[0])
        # print(selected_points[1])
        for point1 in selected_points:
            for point2 in selected_points:
                if is_adjacent(point1, point2) and point1 != point2:   
                    line = tuple(sorted((point1, point2)))
                    
                    for cell in cells:
                        for edge_index, edge in enumerate(cell.edges):
                            edge = tuple(sorted((edge[0], edge[1])))

                            x1, y1 = line[0]
                            x2, y2 = line[1]
                            x3, y3 = edge[0]
                            x4, y4 = edge[1]

                            if math.sqrt((x3 - x1)**2 + (y3 - y1)**2) <= 2\
                                and math.sqrt((x4 - x2)**2 + (y4 - y2)**2) <= 2:
                                cell.sides[edge_index] = True
                                # print("ff")
                                
                                print("--------")
                                print(line)
                                print(edge)
                                print("-------")
                                print(cell.edges)

                                print(str(edge_index) + " " + str(cells.index(cell))) 
                                print("adiacent")
                                draw_line(point1, point2, (130, 208, 209), cells)
                                selected_points = []
                            # print("linie nu buna")
                    
                    # for point in selected_points:
                    #     pygame.draw.circle(win, (130, 109, 168), point, DOT_RADIUS + 4)
                
                    
        if len(selected_points) >= 8:
        #     #reset selection
            selected_points = []

# draw colored dots when it is selected
def draw_circle(x, y, color):
    # pygame.draw.circle(win, color, (c * cell_size + padding_width, r * cell_size + padding_height), DOT_RADIUS + 4)
    pygame.draw.circle(win, color, (x, y), DOT_RADIUS + 4)

# check if mouse click is inside the cell
def collide_circle(cell, pos):
    circle_radius = DOT_RADIUS + cell_size / 8

    px, py = pos
    cx, cy = cell.rect.topleft
    if (px - cx)**2 + (py - cy)**2 <= circle_radius**2:
        return (True, 0)
    
    cx, cy = cell.rect.topright
    if (px - cx)**2 + (py - cy)**2 <= circle_radius**2:
        return (True, 1)
    
    cx, cy = cell.rect.bottomright
    if (px - cx)**2 + (py - cy)**2 <= circle_radius**2:
        return (True, 2)
    
    cx, cy = cell.rect.bottomleft
    if (px - cx)**2 + (py - cy)**2 <= circle_radius**2:
        return (True, 3)
    
    
    return (False, -1)