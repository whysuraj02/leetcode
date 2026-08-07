class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for num in arr:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        myset = set()
        for value in dic.values():
            if value in myset:
                return False
                break
            else:
                myset.add(value)
        return True