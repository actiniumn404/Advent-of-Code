data = open('inputs/day 4.txt').read().splitlines()
nums = list(map(int, data[0].split(",")))
boards = "\n".join(data[2:]).split("\n\n")
fin = False
for i in range(len(boards)):
    sub_board = []
    for j in range(len(boards[i].split("\n"))):
        sub_board2 = []
        for k in range(len( boards[i].split("\n")[j].split(" ") )):
            if boards[i].split("\n")[j].split(" ")[k] != "":
                sub_board2.append(int( boards[i].split("\n")[j].split(" ")[k] ))
        sub_board.append(sub_board2)
    boards[i] = sub_board

def win(board):
    ideal = [-1 for x in range(5)]
    check = [
        board[0] == ideal,
        board[1] == ideal,
        board[2] == ideal,
        board[3] == ideal,
        board[4] == ideal,
        [board[0][0], board[1][0], board[2][0], board[3][0], board[4][0]] == ideal,
        [board[0][1], board[1][1], board[2][1], board[3][1], board[4][1]] == ideal,
        [board[0][2], board[1][2], board[2][2], board[3][2], board[4][2]] == ideal,
        [board[0][3], board[1][3], board[2][3], board[3][3], board[4][3]] == ideal,
        [board[0][4], board[1][4], board[2][4], board[3][4], board[4][4]] == ideal
        #[board[0][0], board[1][1], board[2][2], board[3][3], board[4][4]] == ideal,
        #[board[4][0], board[3][1], board[2][2], board[3][1], board[4][0]] == ideal
    ]
    return any(check)
last = -1
for num in nums:
    if fin:
        break
    for i in range(len(boards)):
        if fin:
            break
        for col in range(len(boards[i])):
            if fin:
                break
            for row in range(len(boards[i][0])):
                if boards[i][col][row] == num:
                    boards[i][col][row] = -1
                    if win(boards[i]):
                        fin = i+1
                        last = num
                        break

if fin:
    winner = boards[fin-1]
    unmarked = 0
    for row in winner:
        for col in row:
            if col >= 0:
                unmarked += col
    print(last * unmarked)
