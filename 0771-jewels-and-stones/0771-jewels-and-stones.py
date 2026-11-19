class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        myset = set(jewels)
        count = 0
        for ch in stones:
            if ch in myset:
                count += 1
        
        return count