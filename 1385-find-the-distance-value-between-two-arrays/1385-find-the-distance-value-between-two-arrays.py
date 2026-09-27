class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        i = 0
        j = 0
        count = 0
        while i < len(arr1):
            valid = True
            while j < len(arr2):
                if abs(arr1[i] - arr2[j]) <= d:
                    valid = False
                    break
                j += 1
            if valid:
                count += 1

            i += 1
            j = 0

        return count

            
                

           

