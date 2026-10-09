class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mydict = {}
        for word in strs:
            sortword = ''.join(sorted(word))
            if sortword in mydict:
                mydict[sortword].append(word)
            else:
                mydict[sortword] = [word]
        result = [mydict[key] for key in mydict]
        return result