import ctypes
import pygame
import game_manager
import math

pygame.init()

# Screen settings
screen_width, screen_height = 1280, 720
win = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Dots and Polygons Menu")

LINE_WIDTH = 8
DOT_RADIUS = 8
DOT_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (240, 240, 240)

# Definirea culorilor pentru jucători
player_colors = [(0, 255, 0), (255, 0, 0)]  # Verde pentru primul jucător, Roșu pentru al doilea jucător
current_player = 0  # Jucătorul curent (0 sau 1)

# initialize variables based on grid size
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


# update variables based on screen resolution
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


# update the coordinates of selected points after resizing the window
def update_points():
    global selected_points
    info = pygame.display.Info()
    updated_points = [(math.floor(x * screen_width / info.current_w), math.floor(y * screen_height / info.current_h)) for x, y in selected_points]
    selected_points = updated_points


# Schimbă jucătorul după fiecare mutare
def switch_player():
    global current_player
    current_player = (current_player + 1) % len(player_colors)  # Schimbă între 0 și 1
    display_current_player()
    #return player_colors[current_player]

# Funcția care afișează jucătorul curent
def display_current_player():
    global current_player
    pygame.draw.rect(win, BACKGROUND_COLOR, (20, 20, 300, 40))
    font = pygame.font.SysFont("Arial", 30)
    text = f"Current Player: Player {current_player + 1}"
    label = font.render(text, 1, player_colors[current_player])
    win.blit(label, (20, 20))
    pygame.display.update()


def draw_background():
    win.fill(BACKGROUND_COLOR)


def draw_grid(cells):
    get_size(cells)
    draw_background()
    
    # draw dots, lines and polygons
    for index, cell in enumerate(cells):
        pygame.draw.circle(win, DOT_COLOR, cell.rect.topleft, DOT_RADIUS)
        pygame.draw.circle(win, DOT_COLOR, cell.rect.topright, DOT_RADIUS)
        pygame.draw.circle(win, DOT_COLOR, cell.rect.bottomright, DOT_RADIUS)
        pygame.draw.circle(win, DOT_COLOR, cell.rect.bottomleft, DOT_RADIUS)

        detect_and_color_surface(cells, game_manager.GameManager().selected_mode)
        for index, side in enumerate(cell.sides):
            if side == True:
                draw_line(cell.edges[index][0],  cell.edges[index][1], (130, 208, 209), cells)

        for index, dot in enumerate(cell.dots):
            if dot == True:
                draw_circle(cell.points[index][0], cell.points[index][1], (130, 109, 168))

    pygame.display.update()


# check if a polygon is completed and draw it
def detect_and_color_surface(cells, mode):
    for cell in cells:
        # detect complete square
        if mode in ["Square", "Mix"] and cell.is_square_complete():
            if cell.color == (0, 0, 0):
                switch_player()
                cell.color = player_colors[current_player]
                # switch_player()
                # print("patrat" + str(current_player))
            pygame.draw.rect(win, cell.color, cell.rect)
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
                if cell.color == (0, 0, 0):
                    cell.color = player_colors[current_player]
                pygame.draw.polygon(win, cell.color, triangle_points)
                draw_line(cell.rect.topleft, cell.rect.topright, (130, 208, 209), cells)
                draw_line(cell.rect.topleft, cell.rect.bottomleft, (130, 208, 209), cells)
                draw_line(cell.rect.topright, cell.rect.bottomleft, (130, 208, 209), cells)
                
                pygame.draw.circle(win, (130, 109, 168), cell.rect.topright, DOT_RADIUS + 4)
                pygame.draw.circle(win, (130, 109, 168), cell.rect.topleft, DOT_RADIUS + 4)
                pygame.draw.circle(win, (130, 109, 168), cell.rect.bottomleft, DOT_RADIUS + 4)

            elif cell.sides[2] and cell.sides[1] and cell.sides[5]:
                triangle_points = [cell.rect.topright, cell.rect.bottomright, cell.rect.bottomleft]
                if cell.color == (0, 0, 0):
                    cell.color = player_colors[current_player]
                
                pygame.draw.polygon(win, cell.color, triangle_points)
                draw_line(cell.rect.topright, cell.rect.bottomright, (130, 208, 209), cells)
                draw_line(cell.rect.topright, cell.rect.bottomleft, (130, 208, 209), cells)
                draw_line(cell.rect.bottomleft, cell.rect.bottomright, (130, 208, 209), cells)

                pygame.draw.circle(win, (130, 109, 168), cell.rect.topright, DOT_RADIUS + 4)
                pygame.draw.circle(win, (130, 109, 168), cell.rect.bottomleft, DOT_RADIUS + 4)
                pygame.draw.circle(win, (130, 109, 168), cell.rect.bottomright, DOT_RADIUS + 4)
                

            else:
                continue
            switch_player()
            print("triunghi" + str(current_player))

            cell.winner = "Player"


# verify if there is a dot between lines
def is_point_inside_cell(point, cell):
    return cell.rect.collide_circle(point)


# draw line between dots
def draw_line(start, end, color, cells):
    global lines
    #color = player_colors[current_player]  # Folosește culoarea jucătorului curent
    
    pygame.draw.line(win, color, start, end, LINE_WIDTH)
    pygame.draw.circle(win, (130, 109, 168), start, DOT_RADIUS + 4)
    pygame.draw.circle(win, (130, 109, 168), end, DOT_RADIUS + 4)


# check if two points are adjacent
def is_adjacent(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    # horizontal adjacency
    if abs(abs(x1-x2) - cell_size) <= 1 and abs(y1 - y2) <= 1:
        return True

    # vertical adjacency
    if abs(abs(y1 - y2) - cell_size) <= 1 and abs(x1 - x2) <= 1:
        return True

    # diagonal adjacency
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
    collide, index = collide_circle(cell, pos)
    # if the pos collides with a dot, add the dot's coordinates to the selected_points list
    if collide:
        if cell.points[index] not in selected_points:
            selected_points.append(cell.points[index])


def try_draw_line(cells):
    global selected_points
    # check for each pair of points from selected_points if they are adjacent
    # and if they are draw a line between them
    aux = False

    if len(selected_points) >= 2:
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
                                and math.sqrt((x4 - x2)**2 + (y4 - y2)**2) <= 2\
                                and cell.sides[edge_index] == False:
                                cell.sides[edge_index] = True
                                selected_points = []
                                
                                
                                if aux == False:
                                    draw_line(point1, point2, player_colors[current_player], cells)
                                    switch_player()
                                    print("linie" + str(current_player))
                                    aux = True

                                    
                                #switch_player()
                                
                    
        if len(selected_points) >= 8:
            # reset selection
            selected_points = []
            #switch_player()


# draw colored dots when it is selected
def draw_circle(x, y, color):
    pygame.draw.circle(win, color, (x, y), DOT_RADIUS + 4)


# check if mouse click is inside the cell, check for each corner of the cell
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