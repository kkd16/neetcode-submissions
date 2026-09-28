class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            if len(stk) == 0 or t <= stk[-1][1]:
                stk.append([i, t])

            else:
                while len(stk) > 0 and t > stk[-1][1]:
                    idx, tmp = stk.pop()

                    res[idx] = i - idx

                stk.append([i, t])
        
        return res
            

        
