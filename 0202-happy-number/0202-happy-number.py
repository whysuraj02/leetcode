class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        myset = set()
        while n != 1:
            tot = 0

            for digit in n:
                tot += int(digit) ** 2
            
            if tot == 1:
                return True
            elif tot in myset:
                return False
            else:
                myset.add(tot)
                
            n = str(tot)

        return False
