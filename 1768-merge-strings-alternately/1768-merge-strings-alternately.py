class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        min_len=min(len(word1),len(word2))

        for i in range(min_len):
            result += word1[i] + word2[i]
        
        if min_len == len(word1):
            result += word2[min_len:]
        else:
            result += word1[min_len:]
        
        return result