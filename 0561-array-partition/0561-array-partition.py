class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        tot = 0
        while i < len(nums):
            low = min(nums[i],nums[i+1])
            tot += low
            i += 2
        return tot