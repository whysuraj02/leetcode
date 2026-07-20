class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_can=max(candies)
        bool_list=[]
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_can:
                bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list