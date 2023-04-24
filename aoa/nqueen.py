board = [0]*20
count = 0

def print_board(n):
    global count
    print(f"\n Solution {count+1} : \n")
    for i in range(1, n+1):
        print('\t',i,end='')
    for i in range(1, n+1):
        print(f"\n{i}", end='')
        for j in range(1, n+1):
            if board[i] == j:
                print("\tQ", end='')
            else:
                print("\t-", end='')
    count += 1
    print("\n------------------------------------------------------------------------------------------------\n")

def place(row, column):
    for i in range(1, row):
        if board[i] == column or abs(board[i] - column) == abs(i - row):
            return False
    return True

def queen(row, n):
    for column in range(1, n+1):
        if place(row, column):
            board[row] = column
            if row == n:
                print_board(n)
            else:
                queen(row+1, n)

n = int(input("\n Enter the Number of Queens : "))
queen(1, n)
