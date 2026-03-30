class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # bucket sort
        # we know lowercase letters only [a-z]

        out = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')

                counts[idx] = counts[idx] + 1
            
            out[tuple(counts)].append(s)
        
        return list(out.values())
        