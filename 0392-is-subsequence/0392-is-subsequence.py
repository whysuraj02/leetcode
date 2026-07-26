class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = 0
        m = 0
        if len(s) == 0:
            return True
        while n < len(s) and m < len(t):
            if s[n] == t[m]:
                n += 1
            m += 1
        if n < len(s):
            return False
        else:
            return True