import draw
import cell_class
import pygame
import detect_surface


class GameManager:
    _instance = None
    
    def __init__(self):
        self.selected_mode = "Mix"
        

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance


    def run(self):
        # add cells
        cells = []
        nr = 0
        for c in range(draw.cols):
            for r in range(draw.rows):
                nr = nr + 1
                cell = cell_class.Cell(r, c, draw.cell_size, draw.padding_width, draw.padding_height)
                cells.append(cell)
        print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN" + str(nr))

        running = True
        pos = ()
        draw.draw_grid(cells)

        while running:
            # print(draw.selected_points)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    draw.draw_grid(cells)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    inside = False
                    # check if a dot was selected
                    for cell in cells:
                        collide, index = draw.collide_circle(cell, pos)
                        if pos and collide:
                            inside = True
                            # print(cell.rect)
                            # print(pos)
                            # print(str(index) + " " + str(cell.points[index][0]) + " " + str(cell.points[index][1]))
                            draw.draw_circle(cell.points[index][0], cell.points[index][1], (130, 109, 168))
                            cell.dots[index] = True
                            # if cell.r * draw.grid_size + cell.c - 1 >= 0:
                            #     cells[cell.r * draw.grid_size + cell.c - 1].dots[1] = True
                            # if (cell.r - 1) * draw.grid_size + cell.c - 1 < draw.grid_size:
                            #     cells[(cell.r - 1) * draw.grid_size + cell.c + 1].dots[1] = True
                            # if cell.r * draw.grid_size + cell.c - 1 >= 0:
                            #     cells[cell.r * draw.grid_size + cell.c - 1].dots[1] = True
                            # if cell.r * draw.grid_size + cell.c - 1 >= 0:
                            #     cells[cell.r * draw.grid_size + cell.c - 1].dots[1] = True

                            draw.select_point(cell, pos)
                    # if inside == False:
                    #     draw.selected_points = []
                    draw.try_draw_line(cells)
                    pos = (-1, -1)

                            # break
                    draw.detect_and_color_surface(cells, self.selected_mode)



            
            # for line in draw.lines:
            #     pygame.draw.line(draw.win, (130, 208, 209), line[0], line[1], draw.LINE_WIDTH)

            # for r in range(draw.rows):
            #     for c in range(draw.cols):
            #         point = ((c + 1) * draw.cell_size + draw.padding_width, (r + 1) * draw.cell_size + draw.padding_height)
                    # if point in draw.connected_points:
                    #     pygame.draw.circle(draw.win, (130, 109, 168), point, draw.DOT_RADIUS + 4)
                    # else:
                        # pygame.draw.circle(draw.win, draw.DOT_COLOR, point, draw.DOT_RADIUS)

            

            pygame.display.update()

        pygame.quit()