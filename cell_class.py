import pygame

class Cell:
    def __init__(self, r, c, cell_size, padding_width, padding_height):
        
        self.color = (0, 0, 0)
        # row
        self.r = r

        # column
        self.c = c

        # index of cell
        # self.index = r * draw.rows + c

        # rectangle of current cell
        self.rect = pygame.Rect(c * cell_size + padding_width, r * cell_size + padding_height, cell_size, cell_size)

        # available edges
        top_edge = ((self.rect.left, self.rect.top), (self.rect.right, self.rect.top))  # Horizontal edge at the top
        bottom_edge = ((self.rect.left, self.rect.bottom), (self.rect.right, self.rect.bottom))  # Horizontal edge at the bottom
        left_edge = ((self.rect.left, self.rect.top), (self.rect.left, self.rect.bottom))  # Vertical edge on the left
        right_edge = ((self.rect.right, self.rect.top), (self.rect.right, self.rect.bottom))  # Vertical edge on the right
        diag1_edge = ((self.rect.left, self.rect.top), (self.rect.right, self.rect.bottom))
        diag2_edge = ((self.rect.right, self.rect.top), (self.rect.left, self.rect.bottom)) 

        # available edges
        self.edges = [
            top_edge, right_edge, bottom_edge, left_edge, diag1_edge, diag2_edge
        ]

        # points of the cell
        self.points = [
            self.rect.topleft, self.rect.topright, self.rect.bottomright, self.rect.bottomleft
        ]

        # true if a line has been drawn for the corresponding edge
        # first 4 are used for squares, the others are used for triangles
        self.sides = [False, False, False, False, False, False]

        self.dots = [False, False, False, False]

        # Winner who completed the square
        self.winner = None


    def is_square_complete(self):
        return all(self.sides[:4])


    def is_triangle_complete(self):
        return (self.sides[0] and self.sides[2] and self.sides[4]) or (self.sides[1] and self.sides[3] and self.sides[5])
    
    
    def update_dim(self, cell_size, padding_width, padding_height):
        self.rect = pygame.Rect((self.c + 1) * cell_size + padding_width, (self.r + 1) * cell_size + padding_height, cell_size, cell_size)

        # available edges
        top_edge = ((self.rect.left, self.rect.top), (self.rect.right, self.rect.top))  # Horizontal edge at the top
        bottom_edge = ((self.rect.left, self.rect.bottom), (self.rect.right, self.rect.bottom))  # Horizontal edge at the bottom
        left_edge = ((self.rect.left, self.rect.top), (self.rect.left, self.rect.bottom))  # Vertical edge on the left
        right_edge = ((self.rect.right, self.rect.top), (self.rect.right, self.rect.bottom))  # Vertical edge on the right
        diag1_edge = ((self.rect.left, self.rect.top), (self.rect.right, self.rect.bottom))
        diag2_edge = ((self.rect.right, self.rect.top), (self.rect.left, self.rect.bottom)) 

        # available edges
        self.edges = [
            top_edge, right_edge, bottom_edge, left_edge, diag1_edge, diag2_edge
        ]

        # points of the cell
        self.points = [
            self.rect.topleft, self.rect.topright, self.rect.bottomright, self.rect.bottomleft
        ]

def is_board_full(cells, mode):
    all_complete = True
    for i, cell in enumerate(cells):
        if not cell.is_square_complete():
            print(f"Cell {i} incomplete for squares: {cell.sides[:4]}")
            all_complete = False

    if all_complete:
        print("Board is full.")
    return all_complete
