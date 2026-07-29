class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic={}
        for ch in s:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1

        for ch in t:
            if ch in dic and dic[ch] > 0:
                dic[ch] -= 1
            else:
                return ch
