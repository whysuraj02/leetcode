class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        left = 0
        while left < len(s):
            right = min(left+k,len(s))
            s[left : right] = s[left : right] [::-1]
            left += 2 * k
        return "".join(s)
