class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        myset = set(banned)
        total = 0
        count = 0
        for i in range(1,n+1):
            if i in myset:
                continue
            else:
                if total + i > maxSum:
                    break
                else:
                    total += i
                    count += 1

        return count


