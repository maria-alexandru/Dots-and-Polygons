import pygame

class Cell:
    def __init__(self, r, c, cell_size, padding_width, padding_height):
        # row
        self.r = r

        # column
        self.c = c

        # index of cell
        # self.index = r * draw.rows + c

        # rectangle of current cell
        self.rect = pygame.Rect((c + 1) * cell_size + padding_width, (r + 1) * cell_size + padding_height, cell_size, cell_size)

        # available edges
        self.edges = [
            [self.rect.topleft, self.rect.topright, self.rect.bottomleft, self.rect.bottomright]
        ]

        # true if a line has been drawn for the corresponding edge
        # first 4 are used for squares, the others are used for triangles
        self.sides = [False, False, False, False, False, False]

        # Winner who completed the square
        self.winner = None

    def is_square_complete(self):
        return all(self.sides[:4])

    def is_triangle_complete(self):
        return (self.sides[0] and self.sides[2] and self.sides[4]) or (self.sides[1] and self.sides[3] and self.sides[5])