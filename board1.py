import numpy as np
from move import Move
from Player import Player
from tabulate import tabulate


class Board:
    EMPTY_CELL = 0

    def __init__(self):
        # self._gameboard = np.zeros(9, dtype=int).reshape(3, 3)
        self._gameboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def print_board(self):
        print("\nPositions")
        self.print_board_with_positions()
        print("Board :")
        for row in self._gameboard:
            # print(row)
            print("|", end="")
            for column in row:
                if column == Board.EMPTY_CELL:
                    # print(column)
                    print("   |", end="")
                else:
                    print(f" {column} |", end="")
            print()
        print()

    def print_board_with_positions(self) -> None:
        print(
            tabulate(np.arange(1, 10, dtype=int).reshape(3, 3), tablefmt="simple_grid")
        )

    def submit_move(self, player: Player, move: Move) -> None:
        # Method for placing the markers
        row = move.get_row()
        # print("type of row : ", row)
        col = move.get_column()
        # print("type of Col : ", col)
        value = self._gameboard[row][col]

        if value == Board.EMPTY_CELL:
            # This is where the markers are placed
            self._gameboard[row][col] = player.marker
        else:
            print("This position is already taken. Please enter another one")

    def check_game_over(self, player: Player, last_move: Move):
        return (
            (self.check_row(player, last_move))
            or (self.check_col(player, last_move))
            or (self.check_diagonal(player))
            or (self.check_antidiagonal(player))
        )

    def check_row(self, player: Player, last_move: Move):
        row_index = last_move.get_row()  # e.g. 1
        board_row = self._gameboard[row_index]  # e.g. row 1 - ['X','O','X']
        # print(board_row)
        # print(board_row.count(player.marker))
        return board_row.count(player.marker) == 3

    def check_col(self, player: Player, last_move: Move):
        col_index = last_move.get_column()  # e.g.0
        board_col = [
            self._gameboard[row][col_index] for row in range(3)
        ]  # e.g. ['X','X','X']
        # print(board_col)
        # print(board_col.count(player.marker))
        return board_col.count(player.marker) == 3

    def check_diagonal(self, player):
        marker_count = 0
        for i in range(3):
            if self._gameboard[i][i] == player.marker:
                marker_count = marker_count + 1

        return marker_count == 3

    def check_antidiagonal(self, player: Player):
        marker_count = 0
        for i in range(3):
            if self._gameboard[i][2 - i] == player.marker:
                marker_count = marker_count + 1

        return marker_count == 3

    # Check Tie and Reset board
    def check_is_tie(self):
        empty_counter = 0

        for row in self._gameboard:
            empty_counter = empty_counter + row.count(Board.EMPTY_CELL)

        return empty_counter == 0

    def reset_board(self):
        print()
        print("Resetting the board.....")
        self._gameboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.print_board()


# Testing
# board = Board()
# human_player = Player(is_human=True)
# comp_player = Player(is_human=False)


# board.print_board()

# while not board.check_is_tie():
#     hmove = human_player.get_move()
#     board.submit_move(human_player, hmove)
#     board.print_board()

#     cmove = comp_player.get_move()
#     board.submit_move(comp_player, cmove)
#     board.print_board()

# print("Its a tie")
# board.reset_board()
