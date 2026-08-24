class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = 0
        
        while i < len(word):
            if word[i] != ch:
                i += 1
            else:
                return word[i::-1]+word[i+1:]
        return word