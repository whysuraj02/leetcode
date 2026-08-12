class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        i = 1

        while i < len(nums):
            if nums[k-1] != nums[i]:
                nums[k] = nums[i]
                k += 1
                i += 1
            else:
                i += 1
        return k
