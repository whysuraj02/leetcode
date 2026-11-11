class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        count = 0
        for key in freq:
            if k > 0:
                if key + k in freq:
                    count += 1
            else:
                if freq[key] > 1:
                    count += 1
        return count
