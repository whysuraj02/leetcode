class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        count = 0
        for i in range(len(nums)):
            for j in range(n):
                if nums[i] > nums[j]:
                    count += 1
            res.append(count)
            count = 0
        return res
