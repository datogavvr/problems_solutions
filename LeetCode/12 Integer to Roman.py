class Solution:
    def intToRoman(self, num: int) -> str:
        M = ["M", "MM", "MMM"]
        C = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        num = str(num)[::-1]
        res = ""
        for i in range(len(num)):
            if i == 0:
                if int(num[i]) > 0:
                    res = I[int(num[i]) - 1]
            elif i == 1:
                if int(num[i]) > 0:
                    res = X[int(num[i]) - 1] + res
            elif i == 2:
                if int(num[i]) > 0:
                    res = C[int(num[i]) - 1] + res
            else:
                if int(num[i]) > 0:
                    res = M[int(num[i]) - 1] + res
        return res
