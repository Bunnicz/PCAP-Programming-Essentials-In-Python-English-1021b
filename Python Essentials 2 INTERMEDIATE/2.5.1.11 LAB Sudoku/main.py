sudoku = []
for i in range(1, 10):
    while True:
        row = input(f'{i}: ')
        row = row.strip()
        if row.isdigit() and len(row) == 9:
            break
        else:
            print("Wrong input")
    sudoku.append(row)

# Sample output: "Yes"
# sudoku = ['295743861',
#           '431865927',
#           '876192543',
#           '387459216',
#           '612387495',
#           '549216738',
#           '763524189',
#           '928671354',
#           '154938672']

# Sample output: "No - square"
# sudoku = ['195743862',
#           '431865927',
#           '876192543',
#           '387459216',
#           '612387495',
#           '549216738',
#           '763524189',
#           '928671354',
#           '254938671']

checksum = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
cond = False
while not cond:
    # check rows
    for row in sudoku:
        check_row = sorted(row)
        if check_row == checksum:
            cond = True
            continue
        else:
            cond = False
            break
    # Stop checking if False
    if not cond:
        print("No - row")
        break

    # check columns
    for i in range(9):
        check_col = []
        for j in range(9):
            check_col.append(sudoku[j][i])
        check_col = sorted(check_col)
        if check_col == checksum:
            cond = True
            continue
        else:
            cond = False
            break
    # Stop checking if False
    if not cond:
        print("No - col")
        break

    # check small squares
    for m in range(3):
        for k in range(3):
            check_square = []
            for i in range(k * 3, 3 * (k + 1)):
                for j in range(m * 3, 3 * (m + 1)):
                    check_square.append(sudoku[i][j])
            check_square = sorted(check_square)
            if check_square == checksum:
                cond = True
                continue
            else:
                cond = False
                break
    # Stop checking if False
    if not cond:
        print("No - square")
        break
else:
    print("Yes")
