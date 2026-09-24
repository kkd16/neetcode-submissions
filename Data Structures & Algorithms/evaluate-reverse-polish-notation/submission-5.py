import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stk = []

        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        for t in tokens:

            if t in ops:
                b = stk.pop()
                a = stk.pop()

                op = ops[t]
                res = op(a, b)
                stk.append(int(res))

            else:
                stk.append(int(t))

        return stk[0]

        