class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        for ch in s.lower():
            if ch.isalnum():
                r += ch
        n = len(r)
        i = 0
        j = n - 1
        while i < j:
            if r[i] != r[j]:
                return False
            else:
                i += 1
                j -= 1

        return True