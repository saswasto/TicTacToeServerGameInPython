import random


def sum(a, b, c):
    return a + b + c


def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else ' ')
    one = 'X' if xState[1] else ('O' if zState[1] else ' ')
    two = 'X' if xState[2] else ('O' if zState[2] else ' ')
    three = 'X' if xState[3] else ('O' if zState[3] else ' ')
    four = 'X' if xState[4] else ('O' if zState[4] else ' ')
    five = 'X' if xState[5] else ('O' if zState[5] else ' ')
    six = 'X' if xState[6] else ('O' if zState[6] else ' ')
    seven = 'X' if xState[7] else ('O' if zState[7] else ' ')
    eight = 'X' if xState[8] else ('O' if zState[8] else ' ')
    print(f"{zero}|{one}|{two}")
    print("-+-+-")
    print(f"{three}|{four}|{five}")
    print("-+-+-")
    print(f"{six}|{seven}|{eight}")


def checkwin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X wins!")
            return True
        elif sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("O wins!")
            return True
    return False


if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("::Welcome to your Tic Tac Toe game::\n")
    while True:
        printBoard(xState, zState)

        if turn == 1:
            print("X's turn")
            value = int(input("Please enter a value (0-8): "))
            if xState[value] == 0 and zState[value] == 0:
                xState[value] = 1
                if checkwin(xState, zState):
                    break
                turn = 2
            else:
                print("Invalid move. Please try again.")
        else:
            print("O's turn")
            # Computer's move
            possible_moves = [i for i in range(9) if xState[i] == 0 and zState[i] == 0]
            if len(possible_moves) > 0:
                value = random.choice(possible_moves)
                zState[value] = 1
                if checkwin(xState, zState):
                    break
                turn = 1

