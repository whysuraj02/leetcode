class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = sorted(score, reverse= True)
        dic = {}
        for i in range(len(rank)):
            dic[rank[i]] = i + 1
        
        ans = []
        for num in score:
            if dic[num] == 1:
                ans.append("Gold Medal")
            elif dic[num] == 2:
                ans.append("Silver Medal")
            elif dic[num] == 3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(dic[num]))
        return ans
            
