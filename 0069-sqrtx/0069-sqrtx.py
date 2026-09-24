class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l = 0
        h = x // 2
        ans = 0
        while l <= h:
            mid = (l + h) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                h = mid -1
        return ans