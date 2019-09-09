print('Welcome to Tic Tac Toe !')

def replay():
    return input('Would you like to play again? y/n : ').lower()
    
while True:
    test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    print('Kindly note the following positions for your choice of input\n')
    print(' 1 '+'|'+' 2 '+'|'+' 3 ')
    print('---|---|---')
    print(' 4 '+'|'+' 5 '+'|'+' 6 ')
    print('---|---|---')
    print(' 7 '+'|'+' 8 '+'|'+' 9 \n')

    import random

    def display_board(board):
        print('\n')
        print(' '+board[1]+' '+'|'+' '+board[2]+' '+'|'+' '+board[3]+' ')
        print('---|---|---')
        print(' '+board[4]+' '+'|'+' '+board[5]+' '+'|'+' '+board[6]+' ')
        print('---|---|---')
        print(' '+board[7]+' '+'|'+' '+board[8]+' '+'|'+' '+board[9]+' '+'\n')

    def player_input():
        p1 = ''
        p2 = ''
        first = ''
        def choose_first():
            return random.randint(0,1)
        first = choose_first()
        if first == 0:
            while p1 != 'X' and p1 != 'O':
                p1 = input('Player 1, choose between X or O: ').upper()
        else:
            while p2 != 'X' and p2 != 'O':
                p2 = input('Player 2, choose between X or O: ').upper()    
        if p1 == 'X':
            return ('X','O')
        elif p1 == 'O':
            return ('O','X')
        elif p2 == 'X':
            return ('O','X')
        else:
            return ('X','O')
    player1, player2 = player_input()
    print('\nPlayer 1 is: ',player1)
    print('Player 2 is: ',player2)
    print("\nLet's start !")
    display_board(test_board)

    def win_check(board, mark):
        return ((board[1] == board[2] == board[3] == mark) or
                (board[4] == board[5] == board[6] == mark) or
                (board[7] == board[8] == board[9] == mark) or
                (board[1] == board[4] == board[7] == mark) or
                (board[2] == board[5] == board[8] == mark) or
                (board[3] == board[6] == board[9] == mark) or
                (board[1] == board[5] == board[9] == mark) or
                (board[3] == board[5] == board[7] == mark))

    def place_marker(board, marker, position):
        board[position] = marker

    def space_check(board, position):
            return board[position] == ' '

    def full_board_check(board):
        for i in range(0,10):
            if space_check(board, i):
                return False
        return True

    def player1_choice(board):
        position = 1
        while position in range(1,9):
            try:
                position = int(input('Player 1, choose position to place marker :'))
            except ValueError:
                print('Enter a valid number')
                continue
            if space_check(board, position) is False:
                print('Position already filled ! Please try again.')
                continue
            else:
                return position

    def player2_choice(board):
        position = 1
        while position in range(1,9):
            try:
                position = int(input('Player 2, choose position to place marker :'))
            except ValueError:
                print('Enter a valid number')
                continue
            if space_check(board, position) is False:
                print('Position already filled ! Please try again.')
                continue
            else:
                return position

    full = full_board_check(test_board)
    while not full_board_check(test_board):
        flip = True
        result1 = False
        result2 = False
        while flip and result1 == False and result2 == False:
            pos = player1_choice(test_board)
            place_marker(test_board, player1, pos)
            result1 = win_check(test_board, player1)
            display_board(test_board)
            if result1 == True:
                print('Player 1 has won !!')
                break
            flip = False
        if full_board_check(test_board) == True:
            print('Game Drawn...')
            break
        if result1 == True:
            break
        while not flip and result1 == False and result2 == False:
            pos = player2_choice(test_board)
            place_marker(test_board, player2, pos)
            result2 = win_check(test_board, player2)
            display_board(test_board)
            if result2 == True:
                print('Player 2 has won !!')
                break
            flip = True
            full = full_board_check(test_board)
        if result2 == True:
            break
        if full_board_check(test_board) == True and result1 == False and result2 == False:
            print('Game Drawn...')
            break
    ans = replay()
    if ans == 'y':
        continue
    else:
        break
