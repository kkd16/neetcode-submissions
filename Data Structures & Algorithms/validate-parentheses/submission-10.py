class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for c in s:
            if c in pairs.values():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                r = stack.pop()
                if pairs[c] != r:
                    return False

        return len(stack) == 0


        