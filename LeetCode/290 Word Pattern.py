class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = list(map(str, s.split()))
        if len(pattern) != len(s):
            return False
        pattern_matches_s = {}
        s_matches_pattern = {}
        for i in range(len(pattern)):
            if pattern[i] in pattern_matches_s and not s[i] in s_matches_pattern:
                return False
            if not pattern[i] in pattern_matches_s and s[i] in s_matches_pattern:
                return False
            if pattern[i] in pattern_matches_s:
                if not pattern_matches_s[pattern[i]] == s[i]:
                    return False
            else:
                pattern_matches_s[pattern[i]] = s[i]
                s_matches_pattern[s[i]] = pattern[i]
        return True
