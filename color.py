class Colors:
    def __init__(self):
        self.player1_line = (90, 76, 120)
        self.player1_fill = (174, 148, 227)

        self.player2_line = (81, 111, 130)
        self.player2_fill = (129, 206, 227)

        self.background1 = (255, 248, 181)
        self.background2 = (245, 173, 247)

    def get_colors(self):
        return {
            "player1:" {
                "line": self.player1_line
                "fill": self.player1_fill
            },
            "player2": {
                "line": self.player2_line
                "fill": self.player2_fill
            },
            "background1": self.background1
            "background2": self.background2
        }