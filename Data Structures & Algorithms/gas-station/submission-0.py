class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        current_gas = 0
        start = 0
        for i in range(len(gas)):
            if current_gas < 0:
                current_gas = 0
                start = i
            current_gas += gas[i]
            current_gas -= cost[i]

        return start