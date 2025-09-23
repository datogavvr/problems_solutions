class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        elif numRows == 2:
            return s[::2] + s[1::2]
        res = ""
        steps = [[abs((numRows-3)*2) + 4]]
        for i in range(1, numRows-1):
            if i == 1:
                steps.append((steps[i-1][0]-2, 2))
            else:
                steps.append((steps[i-1][0]-2, steps[i-1][1]+2))
        steps.append(steps[0])
        for i in range(numRows):
            ind = i
            mark = True
            while mark:
                for j in steps[i]:
                    if ind >= len(s):
                        mark = False
                        break
                    res += s[ind]
                    ind += j
        return res