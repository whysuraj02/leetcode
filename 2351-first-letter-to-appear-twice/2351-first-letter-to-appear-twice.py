class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dic = {}
        for ch in s:
            if ch in dic:
                return ch
            else:
                dic[ch] = 1