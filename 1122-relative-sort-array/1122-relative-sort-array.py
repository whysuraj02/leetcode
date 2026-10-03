class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        left_num = []
        my_set = set(arr2)
        n1 = len(arr1)
        for i in range(n1):
            if arr1[i] not in my_set:
                left_num.append(arr1[i])
        left_num.sort()
        
        result = []
        
        for num in arr2:
            for j in range(len(arr1)):
                if num == arr1[j]:
                    result.append(arr1[j])
        result.extend(left_num)
        return result


        
                        