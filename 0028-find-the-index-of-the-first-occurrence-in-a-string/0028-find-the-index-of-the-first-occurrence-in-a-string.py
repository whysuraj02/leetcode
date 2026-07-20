class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lenneedle=len(needle)
        for i in range(len(haystack)-lenneedle+1):
            if haystack [i : i+lenneedle] == needle:
                return i
        return -1