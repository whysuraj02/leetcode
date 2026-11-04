class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums.sort()
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        sortfreq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        i = 0
        result = []
        for key,value in sortfreq.items():
            if i == k:
                break
            else:
                i += 1
                result.append(key)
        return result

        

        
        
