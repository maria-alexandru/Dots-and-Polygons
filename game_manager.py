import draw
import cell_class
import pygame

class GameManager:
    _instance = None
    
    def __init__(self):
        self.selected_mode = "Mix"
        self.grid_size = 7


    # singleton
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance


    def run(self):
        draw.init(self.grid_size, self.selected_mode)
        # add cells
        cells = []
        for c in range(draw.cols):
            for r in range(draw.rows):
                cell = cell_class.Cell(r, c, draw.cell_size, draw.padding_width, draw.padding_height)
                cells.append(cell)

        running = True
        pos = ()
        draw.draw_grid(cells)
        draw.display_current_player()

        while running:
            draw.display_current_player()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    draw.draw_grid(cells)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    # check if a dot was selected
                    for cell in cells:
                        collide, index = draw.collide_circle(cell, pos)
                        if pos and collide:
                            draw.draw_circle(cell.points[index][0], cell.points[index][1], (130, 109, 168))
                            cell.dots[index] = True

                            # if a dot was selected, add it to the selected_points
                            draw.select_point(cell, pos)

                    # try to draw a line if 2 adjacent points were selected                   
                    draw.try_draw_line(cells)

                    # reset position
                    pos = (-1, -1)
                       

            pygame.display.update()

        pygame.quit()