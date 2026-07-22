class Solution:
    def reverseVowels(self, s: str) -> str:
        vol_list=['a','A','e','E','i','I','o','O','u','U']
        left = 0
        right = len(s)-1
        s=list(s)
        while left < right:
            if s[left] not in vol_list:
                left += 1
            elif s[right] not in vol_list:
                right -= 1
            else:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
        
        return "".join(s)
            