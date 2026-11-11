class Move:

    def __init__(self, value):
        # print("From init")
        while True:
            if 1 <= value <= 9:
                self.set_value(value)
                break
            else:
                print("Enter a valid value between 1 - 9")
                value = int(input("Try again, enter a number (1-9) or esc to cancel: "))

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def is_valid(self):
        return 1 <= self.__value <= 9

    def get_row(self):
        if self.__value in (1, 2, 3):
            return 0  # first row
        elif self.__value in (4, 5, 6):
            return 1  # second row
        elif self.__value in (7, 8, 9):
            return 2  # third row

    def get_column(self):
        if self.__value in (1, 4, 7):
            return 0  # first column
        elif self.__value in (2, 5, 8):
            return 1  # second column
        elif self.__value in (3, 6, 9):
            return 2  # third column

    value = property(get_value, set_value)


# Testing move
# move = Move(5)
# print(move.value)
# # print("Column :", type(move.get_column()))
# print("Column :", move.get_column())
# # print("Row :", type(move.get_row()))
# print("Row :", move.get_row())
