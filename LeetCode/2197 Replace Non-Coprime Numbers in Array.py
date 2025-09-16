from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = []
        for a in nums:
            while res:
                b = res[-1]
                if gcd(a, b) == 1:
                    break
                a = int(a*b/gcd(a, res.pop()))
            res.append(a)
        return res
