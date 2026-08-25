class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        my_set = set(nums)
        o_k = k
        for i in range(len(nums)):
            if k not in my_set:
                return k
            else:
                k += o_k
        return k
