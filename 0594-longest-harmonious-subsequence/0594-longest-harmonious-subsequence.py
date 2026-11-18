class Solution:
    def findLHS(self, nums: list[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        tot = 0
        for num  in nums:
            if num+1 in freq:
                add = freq[num] + freq[num+1]
                tot = max(tot,add)
        
        return tot

