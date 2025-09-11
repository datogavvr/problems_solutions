class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {}
        for i in 'euioa':
            vowels[i] = 0
            vowels[str.upper(i)] = 0
        for i in s:
            if i in vowels:
                vowels[i] += 1
        for i in list(vowels.keys()):
            if vowels[i] == 0:
                del vowels[i]
        counter = sorted(list(vowels.items()))
        for i in range(len(counter)):
            counter[i] = list(counter[i])
        s = [i for i in s]
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = counter[0][0]
                counter[0][1] -= 1
                if counter[0][1] == 0:
                    counter.pop(0)
        res = ''
        for i in s:
            res += i
        return res