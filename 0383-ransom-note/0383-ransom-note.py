class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_freq = {}
        for char in magazine:
            if char in mag_freq:
                mag_freq[char] += 1
            else:
                mag_freq[char] = 1
        
        for char in ransomNote:
            if char not in mag_freq or mag_freq[char] == 0:
                return False
            else:
                mag_freq[char] -= 1
        return True