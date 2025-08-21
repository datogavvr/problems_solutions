class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        l = len(prefix)
        for i in range(1, len(strs)):
            while strs[i][:l] != prefix[:l]:
                l -= 1
                if l == 0:
                    return ''
            prefix = prefix[:l]
        return prefix 