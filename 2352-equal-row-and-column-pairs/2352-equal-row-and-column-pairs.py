class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        rows = {}
        for nums in grid:
            nums = tuple(nums)
            if nums in rows:
                rows[nums] += 1
            else:
                rows[nums] = 1
        ans = 0
        for j in range(len(grid)):
            col = tuple(grid[i][j] for i in range(len(grid)))
            ans += rows.get(col,0)
        return ans