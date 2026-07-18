class Board:
    def __init__(self):
        self.grid = [[0 for _ in range(7)] for _ in range(6)]

    def display(self):
        for row in self.grid:
            print(row)

    