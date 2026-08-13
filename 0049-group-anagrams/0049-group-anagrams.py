class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        n = len(strs)
        for word in strs:
            key = ''.join(sorted(word))
            if key not in dic:
                dic[key] = []
            dic[key].append(word)

        return list(dic.values())