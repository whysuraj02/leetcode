class Solution:
    def findLucky(self, arr: list[int]) -> int:
        dict = {}
        for num in arr:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        
        lar = -1
        for key in dict:
            if key == dict[key]:
                if key > lar:
                    lar = key
        return lar