class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        for i in range(len(s) - 2):
        c = 0
            if s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2]:
                c += 1
        return c
"
