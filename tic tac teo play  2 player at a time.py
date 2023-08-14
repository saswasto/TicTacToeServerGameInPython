def sum(a, b, c):
    return a + b + c

def printBoard(xState, zState):
    zero = 'x' if xState[0] else ('0' if zState[0] else 0)
    one = 'x' if xState[1] else ('0' if zState[1] else 1)
    two = 'x' if xState[2] else ('0' if zState[2] else 2)
    three = 'x' if xState[3] else ('0' if zState[3] else 3)
    four = 'x' if xState[4] else ('0' if zState[4] else 4)
    five = 'x' if xState[5] else ('0' if zState[5] else 5)
    six = 'x' if xState[6] else ('0' if zState[6] else 6)
    seven = 'x' if xState[7] else ('0' if zState[7] else 7)
    eight = 'x' if xState[8] else ('0' if zState[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five}")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight}")

def checkwin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X wins!")
            return True
        elif sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("Z wins!")
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
            value = int(input("Please enter a value: "))
            xState[value] = 1
            if checkwin(xState, zState):
                break
            turn = 2
        else:
            print("Z's turn")
            value = int(input("Please enter a value: "))
            zState[value] = 1
            if checkwin(xState, zState):
                break
            turn = 1

    printBoard(xState, zState)


