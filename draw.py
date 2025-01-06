class Colors:
    def __init__(self):
        # theme 1
        self.player1_line = (129, 181, 129)
        self.player1_fill = (159, 227, 159)

        self.player2_line = (199, 109, 138)
        self.player2_fill = (230, 151, 176)

        self.background0 = (240, 240, 240)
        self.neutral_line0 = (163, 143, 199)
        self.dot0 = (130, 109, 168)

        #theme 2
        self.player11_line = (95, 186, 186)
        self.player11_fill = (160, 232, 232)

        self.player12_line = (67, 110, 93)
        self.player12_fill = (131, 168, 155)

        self.background1 = (249, 232, 250)
        self.neutral_line1 = (143, 101, 112)
        self.dot1 = (158, 135, 173)

        # theme 3
        self.player21_line = (90, 76, 120)
        self.player21_fill = (174, 148, 227)

        self.player22_line = (81, 111, 130)
        self.player22_fill = (129, 206, 227)

        self.background2 = (245, 243, 220)
        self.neutral_line2 = (135, 133, 124)
        self.dot2 = (179, 99, 36)


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
                "line": self.player11_line,
                "fill": self.player11_fill
            },
            "player12": {
                "line": self.player12_line,
                "fill": self.player12_fill
            },
            "player21": {
                "line": self.player21_line,
                "fill": self.player21_fill
            },
            "player22": {
                "line": self.player22_line,
                "fill": self.player22_fill
            },
            "dot0": self.dot0,
            "dot1": self.dot1,
            "dot2": self.dot2,
            "neutral_line0": self.neutral_line0,
            "neutral_line1": self.neutral_line1,
            "neutral_line2": self.neutral_line2,
            "background0": self.background0,
            "background1": self.background1,
            "background2": self.background2
        }
