from Player import Player
from move import Move
from board1 import Board


class TicTocToeGame:

    def __init__(self):
        print("---------------------------")
        print("****Tic Toc Toe Game*******")
        print("---------------------------")

    def game_start(self):

        board = Board()
        human_player = Player(is_human=True)
        compu_player = Player(is_human=False)
        board.print_board()

        while True:
            while True:
                human_move = human_player.get_move()
                board.submit_move(human_player, human_move)
                board.print_board()

                if board.check_is_tie():
                    print("It's a tie, Try again..")
                    break

                elif board.check_game_over(human_player, human_move):
                    print("Awesome you won the game..")
                    break

                else:
                    comp_move = compu_player.get_move()
                    board.submit_move(compu_player, comp_move)
                    board.print_board()

                    if board.check_is_tie():
                        print("It's a tie, Try again..")
                        break
                    elif board.check_game_over(compu_player, comp_move):
                        print("The Computer won the game, Try again")

            play_again = input("To Play Again enter 'x', to quit enter 'o'")

            if play_again == "o":
                print()
                print("See you another time, bye")
                break
            elif play_again == "x":

                self.start_new_round(board)
                self.start()
            else:
                print("Wrong entry, See you another time, bye")

    def start_new_round(self, board):
        print("---------------------------")
        print("****Tic Toc Toe Game ->> New_Round****")
        print("---------------------------")
        board.reset_board()


game1 = TicTocToeGame()
game1.game_start()
