class MinStack:

    def __init__(self):
        self._stk = []
        self._min = []

    def push(self, val: int) -> None:
        self._stk.append(val) 

        if len(self._min) == 0:
            self._min.append(val)
        else:   
            self._min.append(min(self._min[-1], val))    

    def pop(self) -> None:
        self._stk.pop()
        self._min.pop()   

    def top(self) -> int:
        return self._stk[-1]
        
    def getMin(self) -> int:
        return self._min[-1]
        
