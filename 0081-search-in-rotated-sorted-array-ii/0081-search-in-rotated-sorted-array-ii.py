class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l = 0
        h = n-1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] == nums[h]:
                l += 1
                h -= 1
                continue
            #identify the sorted part
            if nums[mid] <= nums[h]:
                if nums[mid] <= target <= nums[h]:
                    l = mid +1
                else:
                    h = mid -1
            else:
                if nums[l] <= target <= nums[mid]:
                    h = mid -1
                else:
                    l = mid +1
        return False
        