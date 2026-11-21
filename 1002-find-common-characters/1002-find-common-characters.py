class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = {}
        for ch in words[0]:
            freq[ch] = freq.get(ch,0) + 1
        
        for word in words[1:]:
            curr = {}

            for ch in word:
                curr[ch] = curr.get(ch,0) + 1
            
            for ch in freq:
                freq[ch] = min(freq[ch] , curr.get(ch , 0))

        ans = []
        for ch in freq:
            for i in range(freq[ch]):
                ans.append(ch)

        return ans
            
                
          