class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        s = set(nums)
        high = max(s)
        low = min(s)
        l= list(s)
        l.sort()
        if len(l) < 3:
            return -1
        else:
            return l[1]