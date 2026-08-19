class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = set(nums)
        l = list(n)
        l.sort()
        if len(l) < 3:
            return max(l)
        else:
            return l[-3]


