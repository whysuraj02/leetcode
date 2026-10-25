class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        bull = 0
        cow = 0
        secr_freq = {}
        gues_freq = {}
        for i in range(n):
            if secret[i] == guess[i]:
                bull += 1
            else:
                secr_freq[secret[i]] = secr_freq.get(secret[i], 0) + 1
                gues_freq[guess[i]] = gues_freq.get(guess[i], 0) + 1
        for key in secr_freq:
            if key in gues_freq:
                cow += min(secr_freq[key],gues_freq[key])

        return str(bull)+ "A" + str(cow) + "B"
