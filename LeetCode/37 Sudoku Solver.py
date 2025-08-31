class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[i // 3 * 3 + j // 3].add(val)

        def possibleValues(i: int, j: int):
            used_values = rows[i] | cols[j] | boxes[i // 3 * 3 + j // 3]
            return {str(i) for i in range(1, 10)} - used_values

        def backtrack():
            min_options = 10
            next_cell = None
            mark = False

            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        options = possibleValues(i, j)
                        options_count = len(options)
                        if options_count == 0:
                            return False
                        if options_count < min_options:
                            min_options = options_count
                            next_cell = (i, j, options)
                        if min_options == 1:
                            mark = True
                            break
                if mark:
                    break
            if next_cell is None:
                return True
            i, j, options = next_cell

            for val in options:
                board[i][j] = val
                rows[i].add(val)
                cols[j].add(val)
                boxes[i // 3 * 3 + j // 3].add(val)

                if backtrack():
                    return True

                board[i][j] = "."
                rows[i].remove(val)
                cols[j].remove(val)
                boxes[i // 3 * 3 + j // 3].remove(val)

            return False

        backtrack()

