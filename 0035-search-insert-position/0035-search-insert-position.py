class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n -1
        ind = n
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] >= target:
                ind = mid
                r = mid -1
            else:
                l = mid +1

        return ind