class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
        sm = nums[l]
        while l <= h:
            mid = (l + h) // 2
            if nums[l] <= nums[mid]:
                if nums[l] <= nums[h]:
                    sm = min(sm,nums[l])
                    h = mid - 1
                else:
                    l = mid  + 1
            else:
                if nums[mid] <= nums[h]:
                    sm = min(sm,nums[mid])
                    h = mid - 1
                else:
                    l = mid + 1
        return sm
            


