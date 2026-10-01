class Solution:
    def firstUniqChar(self, s: str):
        dict = {}
        for ch in s:
            if ch in dict:
                dict[ch] += 1
            else:
                dict[ch] = 1
        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        return -1