class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        half_s = (len(s) // 2) + 1
        for i in range(1,half_s):
            sub = s[:i]
            if sub * (len(s)//i) == s:
                return True
        return False
