class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = s.split()
        if len(pattern) != len(t):
            return False
        dic = {}
        for i in range(len(pattern)):
            if pattern[i] in dic:
                if dic[pattern[i]] != t[i]:
                    return False
            else:
                if t[i] in dic.values():
                    return False
            
            dic[pattern[i]] = t[i]

        return True