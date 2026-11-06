class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        freq = {}
        for word in s1.split():
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        for word in s2.split():
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        result = []
        for key,values in freq.items():
            if values == 1:
                result.append(key)
        
        return result


                