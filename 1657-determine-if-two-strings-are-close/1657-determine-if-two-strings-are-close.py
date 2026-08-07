class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False

        dic = {}
        for char in word1:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1

        dic2 = {}
        for char in word2:
            if char in dic2:
                dic2[char] += 1
            else:
                dic2[char] = 1
        
        if dic.keys() != dic2.keys():
            return False
        
        if sorted(dic.values()) != sorted(dic2.values()):
            return False
        
        return True
