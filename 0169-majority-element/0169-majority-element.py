class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dic = {}
        occur = n/2
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
            
            if dic[num] > occur:
                return num
