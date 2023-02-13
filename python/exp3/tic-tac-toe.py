#amanda saldanha 9574
def draw_board(current_list):
    print("~~~~~~~~~~~~~~~~~")
    print("||",current_list[0],"||",current_list[1],"||",current_list[2],"||")
    print("~~~~~~~~~~~~~~~~~")
    print("||",current_list[3],"||",current_list[4],"||",current_list[5],"||")
    print("~~~~~~~~~~~~~~~~~")
    print("||",current_list[6],"||",current_list[7],"||",current_list[8],"||")
    print("~~~~~~~~~~~~~~~~~")

def get_player_input(player_char,current_list):
    while (player_char!='X')and(player_char!='O'):
        player_char = input(f"{player_char} : please try again :")
    piece_location = int(input(f"{player_char} : where would you like to place your piece :"))
    while piece_location not in range(1,10):
        print(f"{player_char} : that is not a location on the board. try again.")
        piece_location = int(input(f"{player_char} : where would you like to place your piece :"))
    else:
        while current_list[piece_location-1] in ['X','O']:
            print(f"{player_char} : that spot has already been choosen. try again.")
            piece_location = int(input(f"{player_char} : where would you like to place your piece :"))
        else:
            return piece_location-1

def place_char_on_board(player_char,piece_location,current_list):
    if player_char=='X':
        current_list[piece_location]='X'
    else:
        current_list[piece_location]='O'

def is_winner(player_char,current_list):
    winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for positions in winning_positions:
        if all(current_list[pos] == player_char for pos in positions):
            return True
    return False

player_1 = 'X'
player_2 = 'O'
c_list = ['_']*9
n_list = ['1','2','3','4','5','6','7','8','9']

print("welcome to tic tac toe! and the longest 2 hous of my life ;-;")
print("these are the locations on your board!")
draw_board(n_list)
print("this is your current board!")
draw_board(c_list)
print("have fun!")

while '_' in c_list:
    move = get_player_input(player_1,c_list)
    place_char_on_board(player_1,move,c_list)
    draw_board(c_list)
    if is_winner(player_1,c_list):
        print("congratulations player 1! you've won!!")
        break
    if not '_' in c_list:
        print("its a tie!!!")
    
    move = get_player_input(player_2,c_list)
    place_char_on_board(player_2,move,c_list)
    draw_board(c_list)
    if is_winner(player_2,c_list):
        print("congratulations player 1! you've won!!")
        break
    if not '_' in c_list:
        print("its a tie!!!")