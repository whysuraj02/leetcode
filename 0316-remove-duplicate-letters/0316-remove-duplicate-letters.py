class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        my_stack = []
        n = len(s)
        for i in range(n):
            if s[i] in my_stack:
                continue
            
            while my_stack and s[i] < my_stack[-1] and s.find(my_stack[-1], i+1) != -1:
                my_stack.pop()
                    
            my_stack.append(s[i])
        
        return "".join(my_stack)

            