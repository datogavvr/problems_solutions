class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        res = ''
        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            res += '-'
        numerator, denominator = abs(numerator), abs(denominator)
        res += str(numerator // denominator)
        rem = numerator % denominator
        if rem == 0:
            return res
        res += '.'
        remainders = {}
        while rem != 0:
            if rem in remainders:
                return res[:remainders[rem]+1] + '(' + res[remainders[rem]+1:] + ')'
            remainders[rem] = len(res)-1
            res += str(rem*10//denominator)
            rem = rem*10 - rem*10//denominator*denominator
        return res