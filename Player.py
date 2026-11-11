import random
from move import Move

# from
import move


class Player:
    H_PLAYER_MARKER = "X"  # Human Player
    COMPUTER_MARKER = "O"  # Computer Player
    # USER_OPTIONS = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # COMPUTER_OPTION = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __init__(self, is_human=True):
        self.__is_human = is_human
        # User option o/p -  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.__user_options_list = list(range(1, 10))
        # Computer option o/p -  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.__computer_options_list = list(range(1, 10))

        if is_human:
            self.__marker = Player.H_PLAYER_MARKER
        else:
            self.__marker = Player.COMPUTER_MARKER

    @property
    def is_human(self):
        return self.__is_human

    @property
    def marker(self):
        # print(self.__marker)
        return self.__marker

    @property
    def human_options_list(self):
        return self.__user_options_list

    @property
    def comp_options_list(self):
        return self.__computer_options_list

    def get_move(self):
        if self.__is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()

    def get_human_move(self) -> move:
        user_input = int(input("enter a digit between 1-9:"))
        unique_list = set(self.comp_options_list + self.human_options_list)
        return self.validate_move(user_input, unique_list)

        # count = 1
        # while True:
        #     # user_input = int(input("enter a digit between 1-9:"))
        #     if user_input in self.__user_options_list:
        #         self.__user_options_list.remove(user_input)
        #         move = Move(user_input)
        #         return move
        #     elif user_input not in self.__user_options_list:
        #         print(
        #             "Selection not available, choose another number from ",
        #             self.__user_options_list,
        #         )
        #         user_input = int(input("enter a digit between 1-9:"))
        #         count = count + 1
        #         if count == 2:
        #             print(
        #                 "turn loss as you entered the same number again. Moving to other user"
        #             )
        #             break

    def get_computer_move(self) -> move:
        # random_choice = random.choice(list(range(1, 10)))
        unique_list = set(self.comp_options_list + self.human_options_list)
        random_choice = random.choice(list(unique_list))
        return self.validate_move(random_choice, unique_list)
        # while True:
        #     random_choice = random.choice(list(range(1, 10)))
        #     move = Move(random_choice)
        #     return move

    def validate_move(self, player_input, option_list) -> move:
        count = 0
        while True:
            if player_input in option_list:
                option_list.remove(player_input)
                move = Move(player_input)
                return move
            elif player_input not in option_list:
                count = count + 1
                if count == 2:
                    print(
                        "Turn loss as you entered the same number again. Moving to other user"
                    )
                    break
                else:
                    print(
                        "Selection not available, choose another number from \n",
                        option_list,
                    )
                    player_input = int(input("enter a digit between 1-9:"))
                    option_list.remove(player_input)
                    move = Move(player_input)
                    return move


#############################
# Testomg
#############################

# humanplayer = Player(is_human=True)
# hmove = humanplayer.get_move()
# print("hmove.value : ", hmove.value)
# print(humanplayer.marker)
# print("Human player options list :", humanplayer.human_options_list)

# comp_player = Player(is_human=False)
# cmove = comp_player.get_move()
# print("cmove.value : ", cmove.value)
# print(comp_player.marker)
# print("computer_options_list : ", comp_player.comp_options_list)
