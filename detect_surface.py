import pygame
from draw import win

def detect_and_color_surface(cells, mode):
    for cell in cells:
        # detect complete square
        if mode in ["Square", "Mix"] and cell.is_square_complete():
            pygame.draw.rect(win, (0, 255, 0), cell.rect)
            pygame.display.flip()
            cell.winner = "Player"

        if mode in ["Triangle", "Mix"] and cell.is_triangle_complete():
            if cell.sides[0] and cell.sides[2] and cell.sides[4]:
                triangle_points = [cell.rect.topleft, cell.rect.topright, cell.rect.bottomleft]
            elif cell.sides[1] and cell.sides[3] and cell.sides[5]:
                triangle_points = [cell.rect.topright, cell.rect.bottomright, cell.rect.bottomleft]
            else:
                continue

            pygame.draw.polygon(win, (255, 0, 0), triangle_points)
            cell.winner = "Player"