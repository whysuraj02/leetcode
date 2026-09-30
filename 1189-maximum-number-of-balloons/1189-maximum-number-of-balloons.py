class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {}
        for char in text:
            if char in freq:
                freq[char ] += 1
            else:
                freq[char] = 1
        ballon = {
            'b' : 1,
            'a' : 1,
            'l' : 2,
            'o' : 2,
            'n' : 1
        }
        ans = float('inf')
        for char in ballon:
            if char not in freq:
                return 0
            else:
                ans = min(ans,freq[char] // ballon[char])
        return ans