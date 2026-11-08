class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            if nums[left] % 2 == 0 and nums[right] % 2 != 0:
                left += 1
                right -= 1
            elif nums[left] % 2 != 0 and nums[right] % 2 == 0:
                nums[left],nums[right] = nums[right],nums[left]
            elif nums[left] % 2 == 0:
                left += 1
            else:
                right -= 1
        return nums      
