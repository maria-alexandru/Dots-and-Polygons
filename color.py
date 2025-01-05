class Colors:
    def __init__(self):
        # theme 1
        self.player1_line = (90, 76, 120)
        self.player1_fill = (174, 148, 227)

        self.player2_line = (81, 111, 130)
        self.player2_fill = (129, 206, 227)

        self.background1 = (255, 248, 181)
        self.neutral_line0 = (81, 111, 130)

        #theme 2
        self.player12_line = (78, 163, 163)
        self.player12_fill = (160, 232, 232)

        self.player22_line = (84, 161, 132)
        self.player22_fill = (168, 230, 207)

        self.background2 = (245, 173, 247)
        self.neutral_line1 = (84, 161, 132)


    def get_colors(self):
        return {
            "player01": {
                "line": self.player1_line,
                "fill": self.player1_fill
            },
            "player02": {
                "line": self.player2_line,
                "fill": self.player2_fill
            },
            "player11": {
                "line": self.player12_line,
                "fill": self.player12_fill
            },
            "player12": {
                "line": self.player22_line,
                "fill": self.player22_fill
            },
            "neutral_line0": self.neutral_line0,
            "neutral_line1": self.neutral_line0,
            "background0": self.background1,
            "background1": self.background2
        }