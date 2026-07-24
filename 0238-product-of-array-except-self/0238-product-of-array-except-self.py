class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = [1] * n

        left_pro = 1
        for i in range(n):
            result[i] = left_pro
            left_pro *= nums[i]
        
        right_pro = 1
        for i in range(n-1,-1,-1):
            result[i] *= right_pro
            right_pro *= nums[i]
        
        return result