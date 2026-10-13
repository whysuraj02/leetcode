class Solution:
    def numSpecialEquivGroups(self, words: list[str]) -> int:
        myset = set()
        for word in words:
            even = []
            odd = []
            for i in range(len(word)):
                if i % 2 == 0:
                    even.append(word[i])
                else:
                    odd.append(word[i])
        
            myset.add((tuple(sorted(even)),tuple(sorted(odd))))
        
        return len(myset)