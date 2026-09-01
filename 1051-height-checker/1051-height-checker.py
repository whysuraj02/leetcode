class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        i = 0
        mat = 0
        while i < len(heights):
            if heights[i] != expected[i]:
                mat += 1
            i += 1
        return mat