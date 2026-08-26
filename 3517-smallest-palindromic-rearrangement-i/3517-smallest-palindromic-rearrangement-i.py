class Solution:
    def smallestPalindrome(self, s: str) -> str:
        dic = {}
        for ch in s:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1

        l = ""
        m = ""
        for ch in sorted(dic):
            l += ch * (dic[ch] // 2)

            if dic[ch] % 2 != 0:
                m = ch

        r = l[::-1]

        return l+m+r