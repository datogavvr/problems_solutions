class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(n-1):
            s = res
            res = ""
            count = 1
            for i in range(len(s)):
                if i == len(s)-1:
                    res += str(count) + s[i]
                    break
                if s[i] == s[i+1]:
                    count += 1
                else:
                    res += str(count) + s[i]
                    count = 1
        return res
