class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        pro1 = nums[0] * nums[1] * nums[n-1]
        pro2 = nums[n-1] * nums[n-2] * nums[n-3]

        return max(pro1,pro2)