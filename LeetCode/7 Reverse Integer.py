class Solution:
    def reverse(self, x: int) -> int:
        neg = True if x < 0 else False
        x = abs(x)
        l = len(str(x)) # количество цифр в числе
        for i in range(l//2):
            s = x // 10**(l-i-1) % 10 # старший разряд
            m = x // 10**i % 10 # младший разряд
            x = x + (m-s) * 10**(l-i-1) + (s-m) * 10**i
        if x > 2**31:
            return 0
        if neg:
            return -x
        else:
            return x