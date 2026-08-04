class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        set1 = set(nums1)
        set2 = set(nums2)
        ans1 = []
        ans2 = []
        for num in set1:
            if num not in set2:
                ans1.append(num)
        
        for num in set2:
            if num not in set1:
                ans2.append(num)

        return [ans1,ans2]
        # It can also be like this
        # return [list(set1-set2),list(set2-set1)]