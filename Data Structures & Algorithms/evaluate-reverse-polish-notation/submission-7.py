import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    
        ops = {
            "+" : operator.add,
            "-" : operator.sub,
            "*" : operator.mul,
            "/" : operator.truediv
        }

        stk = []

        for t in tokens:
            if t not in ops:
                stk.append(int(t))
            else:
                op = ops[t]
                b = stk.pop()
                a = stk.pop()

                c = op(a, b)
                stk.append(int(c))            

        return stk[-1]