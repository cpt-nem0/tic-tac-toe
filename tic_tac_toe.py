from IPython.display import clear_output
from random import randint


def playerInput():
    player = ''
    while not (player == 'X' or player == 'O'):
        player = input('Player 1 choose either "X" or "O": ').upper()
    if player == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def printBoard():
    clear_output()  # to clear the previous output
    print(
        f'''
        {theBoard[7]}|{theBoard[8]}|{theBoard[9]}
        -+-+-
        {theBoard[4]}|{theBoard[5]}|{theBoard[6]}
        -+-+-
        {theBoard[1]}|{theBoard[2]}|{theBoard[3]}
        '''
    )


def boardStructure():       # structure 'coz of keypad layout
    print("""
    Board Structure:
        (7)|(8)|(9)
        ---+---+---
        (4)|(5)|(6)
        ---+---+---
        (1)|(2)|(3)
    """)


def checkPosition(position):
    return theBoard[position] == ' '


def checkInput(position):
    return position >= 1 or position <= 9


def placePlayer(position, player):
    theBoard[position] = player


def checkWin(player):
    if (theBoard[1] == theBoard[2] == theBoard[3] == player) or \
        (theBoard[4] == theBoard[5] == theBoard[6] == player) or \
        (theBoard[7] == theBoard[8] == theBoard[9] == player) or \
        (theBoard[1] == theBoard[4] == theBoard[7] == player) or \
        (theBoard[2] == theBoard[5] == theBoard[8] == player) or \
        (theBoard[3] == theBoard[6] == theBoard[9] == player) or \
        (theBoard[1] == theBoard[5] == theBoard[9] == player) or \
            (theBoard[3] == theBoard[5] == theBoard[7] == player):
        return True
    else:
        return False


def choosePlayer(p1, p2):
    player = randint(1, 2)
    if player == 1:
        return p1
    else:
        return p2


def checkBoard():
    for i in range(9):
        if checkPosition(i):
            return False
    return True


def replay():
    response = input('play again? "Yes" or "No": ').lower()
    return response == 'yes'


def resetBoard():
    for i in range(1, 10):
        theBoard[i] = ' '


boardStructure()    # board structure for instructions
player1, player2 = playerInput()

theBoard = {7: ' ', 8: ' ', 9: ' ',
            4: ' ', 5: ' ', 6: ' ',
            1: ' ', 2: ' ', 3: ' '}

turn = choosePlayer(player1, player2)
i = 0
while True:
    while i < 9:
        if turn == player1:
            pos = int(input(f'{player1}> '))
        else:
            pos = int(input(f'{player2}> '))
        while True:
            try:
                if checkInput(pos):
                    if checkPosition(pos):
                        placePlayer(pos, turn)

                        if checkWin(turn):
                            printBoard()
                            print(f'player {turn} wins')
                            if replay():
                                i = 0
                                resetBoard()

                        if turn == player1:
                            turn = player2
                        else:
                            turn = player1
                        printBoard()
                        i += 1
                        break
                    else:
                        print('Position already taken.')
                        break
            except KeyError:
                print('Positon must be between 1-9.')
                break

    if i == 9 and not checkWin(turn):
        print("It's a draw !!")
    if replay():
        i = 0
        resetBoard()

    else:
        break
print("Game Ended !!")
