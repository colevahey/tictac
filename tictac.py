from time import sleep as sl
import random

# Board layout
# 0,1,2
# 3,4,5
# 6,7,8

board = '''    1   2   3
   ___ ___ ___
  |   |   |   |
1 | {} | {} | {} |
  |___|___|___|
  |   |   |   |
2 | {} | {} | {} |
  |___|___|___|
  |   |   |   |
3 | {} | {} | {} |
  |___|___|___|
'''

class Location():
    def __init__(self, row, col):
        self.row = row
        self.column = col
        self.occupied = False 
        self.character = " "
    
    def place(self, char):
        self.occupied = True
        self.character = char

spaces = [Location(x,y) for x in range(1,4) for y in range(1,4)]

def print_board():
    print("\033[H\033[2J")
    print(board.format(
        spaces[0].character,
        spaces[1].character,
        spaces[2].character,
        spaces[3].character,
        spaces[4].character,
        spaces[5].character,
        spaces[6].character,
        spaces[7].character,
        spaces[8].character
    ))

def check_winner():

    # Check row winner
    for i in [0,3,6]:
        space = spaces[i]
        if space.row == spaces[i+1].row and space.row == spaces[i+2].row:
            if space.character == spaces[i+1].character and space.character == spaces[i+2].character and space.occupied == True:
                print_board()
                print(space.character, "Wins!")
                exit()

    # Check column winner
    for i in range(0,3):
        space = spaces[i]
        if space.occupied == True and space.character == spaces[i+3].character and space.character == spaces[i+6].character:
            print_board()
            print(space.character, "Wins!")
            exit()

    # Check diagonal winner
    if spaces[0].occupied == True and spaces[0].character == spaces[4].character and spaces[0].character == spaces[8].character:
        print_board()
        print(spaces[0].character, "Wins!")
        exit()
    if spaces[2].occupied == True and spaces[2].character == spaces[4].character and spaces[2].character == spaces[6].character:
        print_board()
        print(spaces[2].character, "Wins!")
        exit()

    # Check CAT
    cat = True
    for space in spaces:
        if space.occupied == False:
            cat = False
        else:
            pass
    if cat == True:
        print("The game ends in a CAT")
        exit()

def multi_player(character):

    if character not in ["X","O"]:
        print("That is not a valid character")
        input("Press enter to restart")
        main()

    while True:
        print_board()
        check_winner()
        try:
            print("It is player "+character+"'s turn")
            columnplace = int(input("In which column would you like to place "+character+"?\n>> "))
            rowplace = int(input("In which row would you like to place "+character+"?\n>> "))
            for space in spaces:
                if space.row == rowplace and space.column == columnplace:
                    if space.occupied:
                        print("That space is already occupied")
                    else:
                        space.place(character)
                        if character == "X":
                            character = "O"
                        else:
                            character = "X"
                    break
        except ValueError:
            print("That is not a row number")
        sl(.5)

def single_player(character):

    if character == "X":
        computer_character = "O"
    elif character == "O":
        computer_character = "X"
    else:
        print("That is not a valid character")
        input("Press enter to restart")
        main()

    while True:
        possible_locations = []
        print_board()
        check_winner()
        try:
            columnplace = int(input("In which column would you like to place "+character+"?\n>> "))
            rowplace = int(input("In which row would you like to place "+character+"?\n>> "))
            for space in spaces:
                if space.row == rowplace and space.column == columnplace:
                    if space.occupied:
                        print("That space is already occupied")
                    else:
                        space.place(character)
                    break
        except ValueError:
            print("That is not a row number")

        print_board()
        sl(.5)
        check_winner()

        # Computer random placing
        for space in spaces:
            if not space.occupied:
                possible_locations.append(space)
        random.choice(possible_locations).place(computer_character)

        sl(.5)

def main():
    game_type = input("\033[H\033[2JWould you like to play single player or multiplayer? (1/2)\n>> ")
    if game_type == "1":
        single_player(input("What character would you like to be? (X/O)\n>> ").title())
    elif game_type == "2":
        multi_player(input("Which character will be going first? (X/O)\n>> ").title())
    else:
        print("That is not a valid game type. Please try again")
        sl(.5)
        main()

main()
