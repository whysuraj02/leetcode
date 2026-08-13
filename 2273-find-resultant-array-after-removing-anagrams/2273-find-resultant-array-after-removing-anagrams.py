class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        dic = {}
        i = 1
        while i < len(words):
            cur = ''.join(sorted(words[i]))
            prev = ''.join(sorted(words[i-1]))

            if cur == prev:
                words.pop(i)
            else:
                i += 1
        return words