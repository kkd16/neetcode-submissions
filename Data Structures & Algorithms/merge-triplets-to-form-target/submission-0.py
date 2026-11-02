class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = False

        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
                
            if a == target[0]:
                x = True
            if b == target[1]:
                y = True
            if c == target[2]:
                z = True

        return x and y and z
        