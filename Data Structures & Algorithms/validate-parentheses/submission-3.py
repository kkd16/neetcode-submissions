class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:

                if len(stack) == 0:
                    return False

                    
                r = stack.pop()

                if c == ')' and r != '(':
                    return False

                if c == '}' and r != '{':
                    return False

                if c == ']' and r != '[':
                    return False
        
        return len(stack) == 0


        