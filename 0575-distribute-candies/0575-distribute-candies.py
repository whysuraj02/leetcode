class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        n = len(candyType)
        caneat = n // 2
        uniquetype = set(candyType)
        noofunitype = len(uniquetype)
        return min(noofunitype,caneat)

            
