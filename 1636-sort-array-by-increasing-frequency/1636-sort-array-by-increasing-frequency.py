class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        
        sorted_dict = sorted(dict.items() , key = lambda x: (x[1] , -x[0]))
        result = []
        for num,count in sorted_dict:
            for i in range(count):
                result.append(num)
        return result

