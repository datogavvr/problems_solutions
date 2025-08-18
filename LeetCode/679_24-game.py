from itertools import permutations, product

class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        tasks = ['(d ? d) ? (d ? d)', '(d ? d ? d) ? d', 'd ? (d ? d ? d)', 'd ? d ? d ? d',
             '((d ? d) ? d) ? d', '(d ? (d ? d)) ? d', 'd ? ((d ? d) ? d)', 'd ? (d ? (d ? d))']
        cards = [str(i) for i in cards]
        digits = list(permutations(cards, 4))
        symbols = list(product(['+', '-', '/', '*'], repeat=3))
        for i in digits:
            for j in symbols:
                for k in tasks:
                    task = k
                    for digit in i:
                        task = task.replace('d', digit, 1)
                    for symbol in j:
                        task = task.replace('?', symbol, 1)
                    try:
                        res = eval(task)
                    except ZeroDivisionError:
                        res = float(10**10)
                    if res - 0.0000001 < 24 and res + 0.0000001 > 24:
                        return True
        return False

s = Solution()
print(s.judgePoint24([1, 2, 3, 4]))