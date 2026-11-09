class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        n = len(piles)
        left = 0
        right = n-1
        you = 0
        while left <= right:
            you += piles[right-1]
            left += 1
            right -= 2
        
        return you
