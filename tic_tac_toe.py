import random


def display_board(board_inserts):
    print('\n')
    print(f'{board_inserts[1]} | {board_inserts[2]} | {board_inserts[3]}')
    print('  |   |')
    print(f'{board_inserts[4]} | {board_inserts[5]} | {board_inserts[6]}')
    print('  |   |')
    print(f'{board_inserts[7]} | {board_inserts[8]} | {board_inserts[9]}')


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O?\n')
        if marker != 'X' and marker != 'O':
            print('Invalid choice')
    player1 = marker
    player2 = 'X' if player1 == 'O' else 'O'
    players = (player1, player2)
    return players


def player_choice_check(board):
    position = 0
    allowed = range(1, 10)
    while position not in allowed or not space_check(board, position):
        position = input('Select the position (1-9):\n')
        try:
            position = int(position)
            if position not in allowed:
                print('Your input is incorrect')
        except ValueError:
            print("That's not an int!")
        
    return position

def player_choice(game_in_live, players):
    
    if step_indicator % 2 == 0:
        print("\nPlayer 1")
        num = player_choice_check(game_in_live)
        if space_check(game_in_live, num):
            game_in_live[num] = players[0]
        
        
    else:
        print("\nPlayer 2")
        num = player_choice_check(game_in_live)
        if space_check(game_in_live, num):
            game_in_live[num] = players[1]


def choose_first():
    rand = random.randint(0,1)
    return rand


def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def replay():
    choice = input('Play again? ("Y"/"N")') 
    return choice == 'Y'

def win_check(game_in_live, mark):
    win_status = False
    keys = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    indicator = 0
    
    while not win_status:
        for each in keys:
            for i in each:
                if game_in_live[i] == mark:
                    indicator += 1
                    if indicator == 3:
                        win_status = True
                        return win_status
                else:
                    indicator = 0
                    break
        break
    return win_status

# Game
status = True
while status:
    board_inserts = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    game_in_live = [' ']*10
    display_board(board_inserts)
    print('\n\n')
    display_board(game_in_live)
    players = player_input()
    temp = True
    first = choose_first()
    if first == 0:
        step_indicator = 0
    else:
        step_indicator = 1
    while temp == True:
        player_choice(game_in_live, players)
        display_board(game_in_live)
        step_indicator += 1
        if  full_board_check(game_in_live):
            temp = False
            print('Draw')
            break
        elif  win_check(game_in_live, players[0]):
            
            print('Congrats 1 Player, you win!')
            break
        elif  win_check(game_in_live, players[1]):
            
            print('Congrats 2 Player, you win!')
            break


    status = replay()
