class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        n = len(nums)
        dic = {}
        for num in nums:
            if num % 2 == 0:
                if num in dic:
                    dic[num] += 1
                else:
                    dic[num] = 1
        ans = -1
        val = 0
        for key,values in dic.items():
            if values > val or (values == val and key < ans):
                ans = key
                val = values
        return ans
        