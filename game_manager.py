import draw
import cell_class
import pygame
from robot_player_class import RobotOpponent
import time
import color

class GameManager:
    _instance = None

    # singleton
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance


    def run(self):
        colors = color.Colors()
        theme_id = 1
        
        draw.set_colors(colors.get_colors(), theme_id)

        if self.opponent == "Computer":
            robot = RobotOpponent()

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
        robot_is_moving = False
 
        while running:
            draw.display_current_player()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    draw.draw_grid(cells)
                elif event.type == pygame.MOUSEBUTTONDOWN and not(draw.current_player == 1 and self.opponent == "Computer"):
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
            draw.display_current_player()  
            pygame.display.update()

            if draw.current_player == 1 and self.opponent == "Computer" and robot_is_moving == False:
                robot_is_moving = True
                points = robot.make_move(cells, self.selected_mode)
                draw.selected_points.append(points[0])
                draw.selected_points.append(points[1])
                draw.try_draw_line(cells)
                robot_is_moving = False
                time.sleep(0.4)
                draw.click_sound.play()

            pygame.display.update()

        pygame.quit()