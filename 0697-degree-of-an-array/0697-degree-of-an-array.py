class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        degree = 1
        first = {}
        last = {}
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                last[nums[i]] = i
                freq[nums[i]] += 1
                if freq[nums[i]] > degree:
                    degree = freq[nums[i]]
            else:
                first[nums[i]] = i
                last[nums[i]] = i
                freq[nums[i]] = 1

        min_length = float('inf')
        for key in freq:
            if freq[key] == degree:
                length = last[key] - first[key] + 1
                min_length = min(min_length,length)
                
        return min_length

        