import draw
import pygame

class Cell:
    def __init__(self, r, c):
        # row
        self.r = r

        # column
        self.c = c

        # index of cell
        self.index = r * draw.rows + c

        # rectangle of current cell
        self.rect = pygame.Rect((c + 1) * draw.cell_size + draw.padding_width, (r + 1) * draw.cell_size + draw.padding_height, draw.cell_size, draw.cell_size)
        self.left = self.rect.left
        self.right = self.rect.right
        self.top = self.rect.top
        self.bottom = self.rect.bottom

        # available edges
        self.edges = [
            [self.rect.topleft, self.rect.topright, self.rect.bottomleft, self.rect.bottomright]
        ]

        # true if a line has been drawn for the corresponding edge
        # first 4 are used for squares, the others are used for triangles
        self.sides = [False, False, False, False, False, False]

        # Winner who completed the square
        self.winner = None
