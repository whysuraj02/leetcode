class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        h = int(c ** 0.5)
        
        while l <= h:
            tot = l *l + h * h 

            if tot == c:
                return True
            elif tot < c:
                l += 1
            else:
                h -= 1
        return False