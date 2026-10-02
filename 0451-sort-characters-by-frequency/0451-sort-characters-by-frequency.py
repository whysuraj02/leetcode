class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        result = ""
        sorted_freq = sorted(freq.items(), key= lambda x: x[1],reverse = True)
        for ch , count in sorted_freq:
            result += ch * count
        return result


        