class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tot = nums[0]
        tot_max = nums[0]
        for i in range(1,len(nums)):
            tot = max(nums[i],tot+nums[i])
            tot_max = max(tot_max,tot)
            
        return tot_max