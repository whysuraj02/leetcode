class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        ans = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1

        while i < m:
            ans.append(nums1[i])
            i += 1
        
        while j < n:
            ans.append(nums2[j])
            j += 1
        if len(ans) % 2 != 0:
            mid = len(ans) // 2
            median = ans[mid]
        else:
            mid = len(ans) // 2
            median = (ans[mid - 1] + ans[mid]) / 2
        
        return median

