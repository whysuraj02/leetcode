class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
                return num
            else:
                dic[num] = 1