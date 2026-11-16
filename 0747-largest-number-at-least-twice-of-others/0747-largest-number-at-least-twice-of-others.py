class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        lar_ind = 0
        lar_num = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > lar_num:
                lar_num = nums[i]
                lar_ind = i
        
        nums.sort()
        if nums[n-2] * 2 > lar_num:
            return -1
        else:
            return lar_ind