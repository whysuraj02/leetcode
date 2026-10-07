class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        freq = {}
        ans = 0
        for num in nums:
            
            if num in freq:
                ans += freq[num]
                freq[num] += 1
            else:
                freq[num] = 1


        return ans
        
        