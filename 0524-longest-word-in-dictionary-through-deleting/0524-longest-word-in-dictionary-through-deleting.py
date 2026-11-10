class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        ans = ""
        for word in dictionary:
            i = 0 #for s
            j = 0 #for word
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            
            if j == len(word):
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word

        return ans
            
