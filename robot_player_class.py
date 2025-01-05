import random
from cell_class import Cell

def get_available_lines(cells):
    available_lines = []
    for cell in cells:
        for index, side in enumerate(cell.sides):
            if not side:
                edge = (cell.edges[index], cell)
                available_lines.append(edge)
    return available_lines
                

class RobotOpponent:
    def __init__(self):
        self.name = "Robot"

    def make_move(self, cells):
        available_edges = get_available_lines(cells)

        if not available_edges:
            return None
        
        selected_edge, selected_cell = random.choice(available_edges)
        edge_start, edge_end = selected_edge

        for index, edge in enumerate(selected_cell.edges):
            if edge == selected_edge:
                selected_cell.sides[index] = True
                break

        return edge_start, edge_end
    

    def play_turn(self, cells, draw_line_function, player_color):
        move = self.make_move(cells)
        if move:
            edge_start, edge_end = move
            if draw_line_function:
                draw_line_function(edge_start, edge_end, (255, 0, 0), cells)
