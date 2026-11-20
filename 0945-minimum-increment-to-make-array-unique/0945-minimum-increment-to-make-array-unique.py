class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        prev = nums[0]
        moves = 0
        n = len(nums)
        for i in range(1,n):
            old = nums[i]
            curr = max(old,prev + 1)

            moves += curr - old
            prev = curr
        
        return moves

        # freq = {}
        # for num in nums:
        #     freq[num] = freq.get(num,0) +1
        
        # n = len(nums)
        # max_num = max(nums)
        # min_num = min(nums)
        # moves = 0
        # for i in range(min_num,max_num + n):
        #     count = freq.get(i,0)

        #     if count > 1:
        #         extra = count -1
        #         moves += extra
        #         freq[i + 1] = freq.get(i+ 1, 0) + extra

        # return moves
