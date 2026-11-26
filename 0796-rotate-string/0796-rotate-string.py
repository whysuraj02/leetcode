class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # return len(s) == len(goal) and goal in s + s

        if len(s) != len(goal):
            return False

        len_s = len(s)

        for _ in range(len_s):
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False
