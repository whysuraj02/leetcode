class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #first method
        set1 = set(nums1)
        set2 = set(nums2)
        ans = []
        for num in set1:
            if num in set2:
                ans.append(num)
        
        return ans

        #second method
        # return list(set(nums1) & set(nums2))

        #third method

        # nums1.sort()
        # nums2.sort()
        # i = 0
        # j = 0
        # ans = []
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] == nums2[j]:
        #         if len(ans) == 0 or ans[-1] != nums1[i]:
        #             ans.append(nums1[i])
        #         i += 1
        #         j += 1
        #     elif nums1[i] < nums2[j]:
        #         i += 1
        #     else:
        #         j += 1
        # return ans
