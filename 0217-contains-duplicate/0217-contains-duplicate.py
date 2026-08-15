class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        dic = {}
        for num in nums:
            if num in dic:
                return True
            else:
                dic[num] = 1
        return False