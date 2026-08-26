class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = "0"
        tot = 0
        for num in str(n):
            if num != "0":
                tot += int(num)
                x += num

        return int(x) * tot