from random import randrange
import sys
print(sys.version)


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   ", board[row][col], "   ", sep="", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    free_move = []

    for place in free_place:  # making list of free moves
        a = place[0] * 3 + place[1] + 1
        free_move.append(a)

    ok = False
    while not ok:
        while True:  # getting input from player
            try:
                move = int(input("Enter your move: "))
                break
            except ValueError:
                print("Warning: the value entered is not a valid number. Try again...")

        ok = 0 < move < 10 and move in free_move    # checking if input is valid
        if ok:
            row = (move - 1) // 3
            col = (move - 1) % 3
            board[row][col] = "O"   # draws player's move on the board
            break
        else:
            print("Not a valid input")
            continue


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    # This function needs to be called first! Other functions relate on global variable free_place
    global free_place
    sign = ["X", "O"]
    free_place = []

    for row in range(3):
        for col in range(3):
            if board[row][col] not in sign:
                free_place.append((row, col))
    return free_place


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    player = None
    if sign == "O":
        player = "player"
    elif sign == "X":
        player = "NPC"
    else:
        print("Error")
        return None

    for i in range(3):
        # Check rows
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return player
        # Check columns
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return player
    # Check diagonals
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign or \
            board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return player
    player = None
    return player  # Currently, nobody won


def draw_move(board):
    # The function draws the computer's random move and updates the board.
    random_move = randrange(len(free_place))
    random_move_place = free_place[random_move]
    board[random_move_place[0]][random_move_place[1]] = "X"


board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]  # Initialise board places 1,2,3...9
board[1][1] = "X"  # Computer puts first move at the center
sign = "O"  # Current player
free_place = make_list_of_free_fields(board)  # initialise global free_place for other functions
display_board(board)

while len(free_place) > 0:
    if sign == "O":
        enter_move(board)
        make_list_of_free_fields(board)
        winner = victory_for(board, sign)
        display_board(board)
        if winner is not None:
            break
        sign = "X"
    elif sign == "X":
        draw_move(board)
        make_list_of_free_fields(board)
        winner = victory_for(board, sign)
        display_board(board)
        if winner is not None:
            break
        sign = "O"

if winner == "player":
    print("You won!")
elif winner == "NPC":
    print("You lost!")
else:
    print("Tie!")