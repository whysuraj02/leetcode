class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                abs_val = abs(nums[i] - nums[j])
                if abs_val == k:
                    count += 1
        return count
