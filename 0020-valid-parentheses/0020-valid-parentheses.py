class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        for bracket in s:
            if len(my_stack) == 0:
                my_stack.append(bracket)
            else:
                if( 
                    (my_stack[-1] == '(' and bracket == ')') or
                    (my_stack[-1] == '{' and bracket == '}') or
                    (my_stack[-1] == '[' and bracket == ']')
                ):
                    my_stack.pop()
                else:
                    my_stack.append(bracket)
        if len(my_stack) == 0:
            return True
        else:
            return False
