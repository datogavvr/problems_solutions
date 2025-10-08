class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        for i in range(len(potions)):  # подсчет, какая мощность должна быть у spell[i] для успеха
            if success < potions[i]:
                potions[i] = 0
            elif success % potions[i] == 0:
                potions[i] = success // potions[i]
            else:
                potions[i] = success // potions[i] + 1
        potions.sort()
        nums = {}
        for i in range(len(potions) - 1, -1, -1):  # сколько зелий имеют одинаковую мощность
            if not potions[i] in nums:
                nums[potions[i]] = i
                potions[i] = [potions[i], 1]
        del nums
        for i in range(len(potions)):  # сколько зелий имеют нужную мощность
            if isinstance(potions[i], list):
                potions[i][1] += i
        potions = [i for i in potions if isinstance(i, list)]
        res = [0] * len(spells)
        for i in range(len(spells)):
            l, r = 0, len(potions) - 1
            while l <= r:
                m = (l + r) // 2
                if spells[i] < potions[m][0]:
                    r = m - 1
                else:
                    l = m + 1
            if potions[r][0] <= spells[i]:
                res[i] = potions[r][1]
        return res
