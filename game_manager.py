import draw
import cell_class
import pygame

# add cells
cells = []
for c in range(draw.COLS):
    for r in range(draw.ROWS):
        cell = cell_class.Cell(r, c)
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
        if event.type == pygame.VIDEORESIZE:
            draw.draw_grid()

    pygame.display.update()

    # check if a dot was selected
    for cell in cells:
        if pos and draw.collide_circle(cell.r, cell.c, pos):
            print(cell.rect)
            draw.draw_circle(cell.r, cell.c, (255, 0, 0))

pygame.quit()