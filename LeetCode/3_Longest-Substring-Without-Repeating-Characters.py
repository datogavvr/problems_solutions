class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subchar = {}
        ans = 0
        i = 0
        while i < len(s):
            if s[i] in subchar:
                i = subchar[s[i]] + 1
                subchar.clear()
            subchar[s[i]] = i
            i += 1
            if len(subchar) > ans:
                ans = len(subchar)
        return ans