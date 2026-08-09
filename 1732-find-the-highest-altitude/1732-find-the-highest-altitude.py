class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        altitudes=[0]
        for i in range(n):
            altitudes.append(altitudes[-1] + gain[i])

        return max(altitudes)

        # n = len(gain)
        # start = 0
        # ans = 0
        # for i in range(n):
        #     start += gain[i]
        #     ans = max(ans,start)
            
        # return ans