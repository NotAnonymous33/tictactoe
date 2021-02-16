class Board:

    def __init__(self, player1, player2):
        self.rows = [[" " for _ in range(3)] for _ in range(3)]
        self.game = True
        self.players = [player1, player2]
        self.current_turns = 0
        self.pieces = ["X", "O"]

    def show_board(self):
        print("----------")
        for row in self.rows:
            print(" | ".join(row))
            print("----------")
        if self.current_turns == 9:
            print("Game has ended in a tie ")
            self.game = False
        else:
            print(f"{self.players[self.current_turns % 2]}'s turn")

    def turn(self):
        self.show_board()
        place = self.get_number() - 1
        row = place // 3
        col = place % 3

        self.rows[row][col] = self.pieces[self.current_turns % 2]
        self.current_turns += 1

    def get_number(self):
        print("Enter a number 1 - 9 ")
        inp = input()
        while len(inp) != 1 or not inp.isdigit() or inp == "0":
            print("Enter a number 1 - 9 ")
            inp = input()
        return int(inp)

    def check(self):
        self.check_rows()
        self.check_colums()
        self.check_diagonals()
        if not self.game:
            print(f"{0} has won", self.current_player)

    def check_rows(self):
        for row in self.rows:
            if len(set(row)) == 1 and set(row)[0] != 0:
                self.game = False

    def check_columns(self):
        pass

    def check_diagonals(self):
        pass


board = Board("One", "Two")
while board.game:
    board.turn()

# DONE Have players and board show up
# Able to put pieces down
# Able to tell whos turn it is
# logic for when someone wins
