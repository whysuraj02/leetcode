class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        my_hash = {}
        ans = []
        for num in nums:
            if num in my_hash:
                my_hash[num] +=1
                ans.append(num)
            else:
                my_hash[num] = 1
                
        # ans = []
        # for key , values in my_hash.items():
        #     if values > 1:
        #         ans.append(key)
        
        return ans
