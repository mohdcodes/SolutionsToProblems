class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def currBox(num, row, col):
            startRow = (row // 3) * 3
            startCol = (col // 3) * 3

            for i in range(startRow, startRow + 3):
                for j in range(startCol, startCol + 3):
                    if (i != row or j != col) and board[i][j] == num:
                        return True
            return False

        def currRow(num, row, col):
            for i in range(9):
                if i != col and board[row][i] == num:
                    return True
            return False

        def currCol(num, row, col):
            for i in range(9):
                if i != row and board[i][col] == num:
                    return True
            return False

        for row in range(9):
            for col in range(9):
                currNum = board[row][col]

                if currNum == ".":
                    continue

                if currRow(currNum, row, col) or currCol(currNum, row, col) or currBox(currNum, row, col):
                    return False

        return True