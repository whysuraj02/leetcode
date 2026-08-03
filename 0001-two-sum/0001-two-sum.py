class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            comp = target -nums[i]
            if comp in dic:
                return [dic[comp],i]
            else:
                dic[nums[i]] = i
        