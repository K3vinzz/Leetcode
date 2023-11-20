def isValidSudoku(board: list[list[str]]) -> bool:
    boxes = [[] for i in range(3)]
    col = [[] for i in range(9)]
    row = []
    for r in range(len(board)):
        row.clear()
        if r % 3 == 0:
            for i in range(3):
                boxes[i].clear()
        for i in range(9):
            if not board[r][i] == ".":
                if board[r][i] not in row:
                    row.append(board[r][i])
                else:
                    return False

                if board[r][i] not in col[i]:
                    col[i].append(board[r][i])
                else:
                    return False

                if i < 3:
                    if board[r][i] not in boxes[0]:
                        boxes[0].append(board[r][i])
                    else:
                        return False
                elif 3 <= i < 6:
                    if board[r][i] not in boxes[1]:
                        boxes[1].append(board[r][i])
                    else:
                        return False
                elif 6 <= i < 9:
                    if board[r][i] not in boxes[2]:
                        boxes[2].append(board[r][i])
                    else:
                        return False
    return True


board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
         [".", "4", ".", "3", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "1"],
         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", "2", ".", "7", ".", ".", ".", "."],
         [".", "1", "5", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "2", ".", ".", "."],
         [".", "2", ".", "9", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."]]

print(isValidSudoku(board))
