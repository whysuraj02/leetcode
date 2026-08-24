class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        my_list = []
        for num in nums:
            sqr = abs(num* num)
            my_list.append(sqr)
        my_list.sort()
        return my_list