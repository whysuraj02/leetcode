class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        carry = 0
        result = ""
        while i >= 0 or j >= 0 or carry:
            dig_a = int(a[i]) if i >= 0 else 0
            dig_b = int(b[j]) if j >= 0 else 0
            add = dig_a + dig_b + carry
            bit = add % 2
            result = str(bit) + result
            carry = add // 2

            i -= 1
            j -=1
        return result