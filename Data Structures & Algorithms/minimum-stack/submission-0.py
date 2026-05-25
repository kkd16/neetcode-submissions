class MinStack:

    def __init__(self):
        self.stk = []
        self.mn = []  

    def push(self, val: int) -> None:
        self.stk.append(val)
        
        if len(self.mn) > 0:
            self.mn.append(min(self.mn[-1], val))
        else:
            self.mn.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.mn.pop()
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.mn[-1]
        
