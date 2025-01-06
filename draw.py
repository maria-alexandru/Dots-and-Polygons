import ctypes
import pygame
import game_manager
import math
from button import Button

pygame.init()
pygame.mixer.init()
click_sound = pygame.mixer.Sound('assets/pop-268648.mp3')
draw_sound = pygame.mixer.Sound('assets/sound-effect-twinklesparkle-115095.mp3')

# Screen settings
screen_width, screen_height = 1280, 720
win = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Dots and Polygons")

LINE_WIDTH = 8
DOT_RADIUS = 8
DOT_COLOR = (0, 0, 0)
background_color = (240, 240, 240)
line_color = (130, 208, 209)
selected_dot_color = (130, 109, 168)

# define colors for players
# green for player 1, red for player 2
player_colors_fill = [(0, 255, 0), (255, 0, 0)]
player_colors_lines = [(0, 255, 0), (255, 0, 0)]
# current_player (0 or 1)
current_player = 0

player1_score = 0
player2_score = 0

# initialize variables based on grid size
def init(size, mode):
    global grid_size, padding_height, padding_width, screen, rows, cols, cell_size,\
           selected_mode, current_player, player1_score, player2_score, selected_points
    grid_size = size
    selected_mode = mode

    rows = cols = grid_size - 1
    cell_size = min(screen_height / (grid_size + 1), screen_width / (grid_size + 1))
    screen = screen_width, screen_height
    padding_width = (screen_width - (grid_size + 1) * cell_size) / 2
    padding_height = (screen_height - (grid_size + 1) * cell_size) / 2

    current_player = 0
    player1_score = 0
    player2_score = 0

    selected_points = []


def set_colors(colors, theme_id):
    global player_colors_fill, player_colors_lines, background_color, line_color, selected_dot_color
    player_colors_fill[0] = colors[f"player{theme_id}1"]["fill"]
    player_colors_fill[1] = colors[f"player{theme_id}2"]["fill"]

    player_colors_lines[0] = colors[f"player{theme_id}1"]["line"]
    player_colors_lines[1] = colors[f"player{theme_id}2"]["line"]

    background_color = colors[f"background{theme_id}"]
    line_color = colors[f"neutral_line{theme_id}"]
    selected_dot_color = colors[f"dot{theme_id}"]


# update variables based on screen resolution
def get_size(cells):
    global screen_width, screen_height, info, padding_height, padding_width, cell_size

    # get the screen resolution (width and height)
    info = pygame.display.Info()
    update_points()
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
    new_screen_width = info.current_w
    new_screen_height = info.current_h
    new_cell_size = min(new_screen_height / (grid_size + 1), new_screen_width / (grid_size + 1))
    new_padding_width = (new_screen_width - (grid_size + 1) * new_cell_size) / 2
    new_padding_height = (new_screen_height - (grid_size + 1) * new_cell_size) / 2

    updated_points = [(math.floor((x - padding_width) // cell_size * new_cell_size + new_padding_width), math.floor((y - padding_height) // cell_size * new_cell_size + new_padding_height)) for (x, y) in selected_points]
    selected_points = updated_points


# change player after each move
def switch_player():
    global current_player
    current_player = (current_player + 1) % len(player_colors_fill)  # Schimba intre 0 si 1

# function that displays current player and score
def display_current_player():
    global current_player, player1_score, player2_score

    text = f"Current Player: Player {current_player + 1}"
    score_text1 = f"Player 1: {player1_score}"
    score_text2 = f"Player 2: {player2_score}"

    scale_factor = min(screen_width / 1280, screen_height / 720)
    font_size = int(20 * scale_factor)
    font = get_font(font_size)
    text_width, text_height = font.size(text)
    text_height += font.size(score_text1)[1]
    pygame.draw.rect(win, background_color, (20, 20, padding_width, screen_height / 2))
    pygame.draw.rect(win, background_color, (20, 20, screen_width / 2, font.size(text)[1]))

    color = player_colors_fill[current_player]
    (r, g, b) = color
    dark = 50
    color = (r - dark, g - dark, b - dark)
    player_label = font.render(text, 1, color)

    color = line_color
    (r, g, b) = color
    color = (r - dark, g - dark, b - dark)
    score_label1 = font.render(score_text1, 1, color)
    score_label2 = font.render(score_text2, 1, color)

    win.blit(player_label, (20, 20))
    win.blit(score_label1, (20, 20 + 1.5 * font.size(text)[1]))
    win.blit(score_label2, (20, 20 + 3 * font.size(text)[1]))

    pygame.display.update()


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

# resize an image according to a scale factor
def scale_image(image, scale_factor):
    width = int(image.get_width() * scale_factor)
    height = int(image.get_height() * scale_factor)
    return pygame.transform.scale(image, (width, height))

def create_button(screen_width, screen_height):
    scale_factor = min(screen_width / 1280, screen_height / 720)
    font_size = int(20 * scale_factor)
    font = get_font(font_size)

    original_image = pygame.image.load("assets/Play Rect.png")
    resized_image = pygame.transform.scale(original_image, (300, 75))
    button_image = scale_image(resized_image, scale_factor)

    menu_button = Button(
        image=button_image,
        pos=(screen_width - button_image.get_width() // 2 - int(20 * scale_factor), button_image.get_height() // 2 + int(20 * scale_factor)),
        text_input=f"BACK TO MENU",
        font=font,
        base_color="White",
        hovering_color="White",
    )
    return menu_button


# find font size for text to fit in max_width
def find_best_font_size(text, max_width):
    font_size = 1
    best_font_size = font_size
    
    while True:
        font = pygame.font.SysFont("lato", font_size, bold = True)
        text_width, text_height = font.size(text)
        if text_width <= max_width:
            best_font_size = font_size
        else:
            break
        font_size += 1

    if best_font_size > 40:
        best_font_size = 40
    return best_font_size
    

def draw_background():
    win.fill(background_color)


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
                draw_line(cell.edges[index][0],  cell.edges[index][1], line_color)

        for index, dot in enumerate(cell.dots):
            if dot == True:
                draw_circle(cell.points[index][0], cell.points[index][1], selected_dot_color)

    pygame.display.update()


def draw_square(cell):
    pygame.draw.rect(win, cell.color, cell.rect)
    draw_line(cell.rect.topleft, cell.rect.topright, line_color)
    draw_line(cell.rect.topright, cell.rect.bottomright, line_color)
    draw_line(cell.rect.bottomright, cell.rect.bottomleft, line_color)
    draw_line(cell.rect.bottomleft, cell.rect.topleft, line_color)
    
    pygame.draw.circle(win, selected_dot_color, cell.rect.topright, DOT_RADIUS + 4)
    pygame.draw.circle(win, selected_dot_color, cell.rect.topleft, DOT_RADIUS + 4)
    pygame.draw.circle(win, selected_dot_color, cell.rect.bottomleft, DOT_RADIUS + 4)
    pygame.draw.circle(win, selected_dot_color, cell.rect.bottomright, DOT_RADIUS + 4)


def draw_triangle(cell, triangle_points):
    if cell.color_tr1_points == triangle_points:
        color = cell.color_tr1
    elif cell.color_tr2 != (0,0,0):
        color = cell.color_tr2

    pygame.draw.polygon(win, color, triangle_points)

    draw_line(triangle_points[0], triangle_points[1], line_color)
    draw_line(triangle_points[1], triangle_points[2], line_color)
    draw_line(triangle_points[2], triangle_points[0], line_color)
    
    pygame.draw.circle(win, selected_dot_color, triangle_points[0], DOT_RADIUS + 4)
    pygame.draw.circle(win, selected_dot_color, triangle_points[1], DOT_RADIUS + 4)
    pygame.draw.circle(win, selected_dot_color, triangle_points[2], DOT_RADIUS + 4)


def set_triangle_color_draw(cell, triangle_points):
    global colored, colored2, player1_score, player2_score, current_player
    if cell.color_tr1 == (0, 0, 0):
        colored = True
        cell.color_tr1 = player_colors_fill[current_player]
        cell.color_tr1_points = triangle_points
        if current_player == 0:
            draw_sound.play()
            player1_score += 1
        else:
            draw_sound.play()
            player2_score += 1

    elif cell.color_tr2 == (0, 0, 0) and cell.color_tr1_points != triangle_points:
        colored2 = True

        cell.color_tr2 = player_colors_fill[current_player]
        cell.color_tr2_points = triangle_points

        if current_player == 0:
            draw_sound.play()
            player1_score += 1
        else:
            draw_sound.play()
            player2_score += 1

    draw_triangle(cell, triangle_points)
    

# check if a polygon is completed and draw it
def detect_and_color_surface(cells, mode):
    global player1_score, player2_score, colored, colored2
    colored = False
    colored2 = False
    switch_player()
    for cell in cells:         
        if mode in ["Triangle", "Mix"] and cell.is_triangle_complete():
            if mode == "Mix" and cell.is_square and not cell.is_triangle:
                continue

            cell.is_triangle = True

            if cell.sides[0] and cell.sides[1] and cell.sides[4]:
                triangle_points = [cell.points[0], cell.points[1], cell.points[2]]
                set_triangle_color_draw(cell, triangle_points)
        
            if cell.sides[2] and cell.sides[3] and cell.sides[4]:
                triangle_points = [cell.points[0], cell.points[2], cell.points[3]]
                set_triangle_color_draw(cell, triangle_points)

            if cell.sides[1] and cell.sides[2] and cell.sides[5]:
                triangle_points = [cell.points[1], cell.points[2], cell.points[3]]
                set_triangle_color_draw(cell, triangle_points)

            if cell.sides[0] and cell.sides[3] and cell.sides[5]:
                triangle_points = [cell.points[0], cell.points[1], cell.points[3]]
                set_triangle_color_draw(cell, triangle_points)

            cell.winner = "Player"
        
        # detect complete square
        if mode in ["Square", "Mix"] and cell.is_square_complete():
            if mode == "Mix" and cell.is_triangle:
                continue
            
            cell.is_square = True

            if cell.color == (0, 0, 0):
                colored = True
                cell.color = player_colors_fill[current_player]
                if current_player == 0:
                    draw_sound.play()
                    player1_score += 1
                else:
                    draw_sound.play()
                    player2_score += 1

            draw_square(cell)
            cell.winner = "Player"

    if colored == False and colored2 == False:
        switch_player()


# verify if there is a dot between lines
def is_point_inside_cell(point, cell):
    return cell.rect.collide_circle(point)


# draw line between dots
def draw_line(start, end, color):
    pygame.draw.line(win, color, start, end, LINE_WIDTH)
    pygame.draw.circle(win, selected_dot_color, start, DOT_RADIUS + 4)
    pygame.draw.circle(win, selected_dot_color, end, DOT_RADIUS + 4)


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
    if abs(abs(x1 - x2) - cell_size) <= 1 and abs(abs(y1 - y2) - cell_size) <= 1\
        and selected_mode in ["Triangle", "Mix"]:
        return True
    return False


# select two dots and draw the line
def select_point(cell, pos):
    global selected_points
    collide, index = collide_circle(cell, pos)
    # if the pos collides with a dot, add the dot's coordinates to the selected_points list
    if collide:
        if not is_in_selected_points(cell.points[index]):
            selected_points.append(cell.points[index])
            click_sound.play()


def is_in_selected_points(point):
    for s_point in selected_points:
        if is_same_point(point, s_point):
            return True
    return False


def is_same_point(point1, point2):
    (x1, y1) = point1
    (x2, y2) = point2
    if abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1:
        return True
    return False


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

                                if selected_mode == "Mix" and cell.is_square_complete() and (edge_index == 4 or edge_index == 5):
                                    continue

                                if selected_mode in ["Triangle", "Mix"]:
                                    if edge_index == 4 and cell.sides[5] == True:
                                        continue
                                    if edge_index == 5 and cell.sides[4] == True:
                                        continue

                                cell.sides[edge_index] = True
                                selected_points = []
                                
                                if aux == False:
                                    draw_line(point1, point2, player_colors_lines[current_player])
                                    switch_player()
                                    aux = True

                    # check if a polygon was completed and draw it
                    detect_and_color_surface(cells, selected_mode)

                elif len(selected_points) >= 1 and point1 != point2:
                    remove_not_selected_dots(cells)

        if len(selected_points) >= 8:
            # reset selection
            selected_points = []

def remove_not_selected_dots(cells):
    last_point = selected_points[-1]
    for s_point in selected_points:
        if last_point and s_point != last_point:
            for cell in cells:
                for index, point in enumerate(cell.points):
                    if is_same_point(s_point, point) and dot_not_in_line(cells, point):
                        # set the dot to false
                        cell.dots[index] = False
                        pygame.draw.circle(win, background_color, point, DOT_RADIUS + 5)
                        pygame.draw.circle(win, DOT_COLOR, point, DOT_RADIUS)
            selected_points.remove(s_point)

    if last_point:
        pygame.draw.circle(win, selected_dot_color, last_point, DOT_RADIUS + 4)               
                    

def dot_not_in_line(cells, point):
    for cell in cells:
        for index, cell_point in enumerate(cell.points):
            if is_same_point(cell_point, point):
                if cell.sides[index] == True:
                    return False
                                    
                elif index >= 1 and cell.sides[index - 1] == True:
                    return False
                
                elif selected_mode in ["Square", "Mix"] and index == 0 and cell.sides[3] == True:
                    return False

                elif selected_mode in ["Triangle", "Mix"] and (index == 0 or index == 2) and cell.sides[4] == True:
                    return False
                
                elif selected_mode in ["Triangle", "Mix"] and (index == 1 or index == 3) and cell.sides[5] == True:
                    return False
    return True


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