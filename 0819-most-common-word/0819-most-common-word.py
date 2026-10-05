class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        my_set = set(banned)
        dict = {}

        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")

        for word in paragraph.lower().split():
            word = word.strip("!?',;.")
            if word not in my_set:
                if word not in dict:
                    dict[word] = 1
                else:
                    dict[word] += 1
        
        mf = 0
        mfw = ""
        for key in dict:
            if dict[key] > mf:
                mf = dict[key]
                mfw = key

        return mfw        