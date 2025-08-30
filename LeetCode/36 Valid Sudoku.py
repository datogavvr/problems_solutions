class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [list() for i in range(9)]
        boxes = [list() for i in range(9)]

        for i in range(9):
            row = []
            for j in range(9):
                cell = board[i][j]

                if cell == ".":
                    continue
                if cell in row or cell in columns[j] or cell in boxes[i // 3 * 3 + j // 3]:
                    return False

                row.append(cell)
                columns[j].append(cell)
                boxes[i // 3 * 3 + j // 3].append(cell)
        return True
