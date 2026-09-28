class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        dic = {}
        occurs = n/3
        my_list = []
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
            
            if dic[num] > occurs:
                if num not in my_list:
                    my_list.append(num)
                    
        return my_list