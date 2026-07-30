class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        l=list(s)
        for i in range(len(s)):
            l[i] = l[i] [::-1]
        return " ".join(l)