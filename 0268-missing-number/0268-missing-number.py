class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        my_set = set(nums)
        for i in range(len(nums)+1):
            if i not in my_set:
                return i
