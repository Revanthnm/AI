
from random import randint


def create_board():
    return [' '] * 9


def display_board(board):
    print('\t-------------------------')
    print('\t|       |       |       |')
    print('\t|   ' + board[0] + '   |   ' +
          board[1] + '   |   ' + board[2] + '   |')
    print('\t|       |       |       |')
    print('\t-------------------------')
    print('\t|       |       |       |')
    print('\t|   ' + board[3] + '   |   ' +
          board[4] + '   |   ' + board[5] + '   |')
    print('\t|       |       |       |')
    print('\t-------------------------')
    print('\t|       |       |       |')
    print('\t|   ' + board[6] + '   |   ' +
          board[7] + '   |   ' + board[8] + '   |')
    print('\t|       |       |       |')
    print('\t-------------------------')


def winning(player, board):
    return(
        board[0] == player and board[1] == player and board[2] == player or
        board[3] == player and board[4] == player and board[5] == player or
        board[6] == player and board[7] == player and board[8] == player or
        board[0] == player and board[3] == player and board[6] == player or
        board[1] == player and board[4] == player and board[7] == player or
        board[2] == player and board[5] == player and board[8] == player or
        board[0] == player and board[4] == player and board[8] == player or
        board[2] == player and board[4] == player and board[6] == player
    )


def board_isfull(board):
    for i in range(1, 10):
        if (board[i-1] == ' '):
            return False
    return True


def isValid(board, pos):
    return (pos > 0 and pos < 10) and board[pos-1] == ' '


def player_turn(board, player):
    pos = input('Your turn enter position : ')
    while (not isValid(board, int(pos))):
        pos = input('Please enter valid position : ')
    board[int(pos) - 1] = player
    display_board(board)


def MiniMax(board, depth, isMax, computer, player):
    if winning(computer, board):
        return 1
    if winning(player, board):
        return -1
    if board_isfull(board):
        return 0

    if isMax:
        best = -100
        for slot, value in enumerate(board):
            if value == ' ':
                board[slot] = computer
                best = max(best, MiniMax(
                    board, depth+1, False, computer, player))
                board[slot] = ' '
        return best
    else:
        best = 100
        for slot, value in enumerate(board):
            if (value == ' '):
                board[slot] = player
                best = min(best, MiniMax(
                    board, depth+1, True, computer, player))
                board[slot] = ' '
        return best


def best_postion(board, computer, player):
    best_pos = -1
    best_weight = -1000
    for slot, value in enumerate(board):
        if (value == ' '):
            board[slot] = computer
            move_weight = MiniMax(board, 0, False, computer, player)
            board[slot] = ' '
            if (best_weight < move_weight):
                best_weight = move_weight
                best_pos = slot
    return best_pos


def computers_turn(board, computer, player):
    pos = best_postion(board, computer, player) + 1
    board[pos - 1] = computer
    print('Computer has played its move at : ', pos)


def available_slot(board):
    return [i for i in range(0, 9) if (board[i] == ' ')]


def tictactoe():
    board = create_board()

    player = input('Choose X | O : ')

    while(not(player == 'X' or player == 'O')):
        player = input('Enter valid option (X|O) : ')

    if (player == 'X'):
        computer = 'O'
    else:
        computer = 'X'

    print('Player = '+player+' \computer = '+computer)
    print('---New board---(index 1-9)')
    display_board(board)

    chance = randint(0, 1)
    while(1):
        if (board_isfull(board)):
            print('Draw')
            break
        if (chance == 1):
            player_turn(board, player)
            if (winning(player, board)):
                print('You ('+player+') won')
                break
            chance = 0
        else:
            computers_turn(board, computer, player)
            display_board(board)
            if (winning(computer, board)):
                print('Player2 ('+computer+') won')
                break
            chance = 1

    again = input('Want to play again (yes|no) : ')
    if (again.lower() == 'yes' or again.lower() == 'y'):
        tictactoe()


tictactoe()
