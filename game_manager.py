import draw
import cell_class
import pygame
import detect_surface

selected_mode = "Square"

# add cells
cells = []
for c in range(draw.cols):
    for r in range(draw.rows):
        cell = cell_class.Cell(r, c, draw.cell_size, draw.padding_width, draw.padding_height)
        cells.append(cell)


running = True
pos = ()
draw.draw_grid()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            for cell in cells:
                draw.select_point(cell.r, cell.c, pos, cells)
        if event.type == pygame.VIDEORESIZE:
            draw.draw_grid()

    detect_surface.detect_and_color_surface(cells, selected_mode)
    pygame.display.update()

    # check if a dot was selected
    for cell in cells:
        if pos and draw.collide_circle(cell.r, cell.c, pos):
            print(cell.rect)
            draw.draw_circle(cell.r, cell.c, (130, 109, 168))


pygame.quit()