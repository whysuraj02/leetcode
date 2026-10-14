class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                correct_ind = nums[i] - 1
                nums[i],nums[correct_ind] = nums[correct_ind],nums[i]
            else:
                i += 1
        
        for i in range(n):
            if i+1 != nums[i]:
                return i+1
        return n+1

        
