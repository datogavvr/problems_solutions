class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        n, m = max(n, m), min(n, m)
        if m == 1:
            return n // 2
        if n % 2 == 1 and m % 2 == 1:
            res = ((m // 2) * (m // 2 + 1) * 2 +
            m * (n - m) // 2)
        elif n % 2 == 0 and m % 2 == 0:
            res = ((m // 2) ** 2 * 2 +
            m * (n - m) // 2)
        elif n % 2 == 1:
            res = ((m // 2) ** 2 * 2 +
            m // 2 * (n - m))
        else:
            res = ((m // 2) * (m // 2 + 1) * 2 +
            (n - m) // 2 * (m // 2) +
            ((n - m) // 2 + 1) * (m // 2 + 1))
        return res