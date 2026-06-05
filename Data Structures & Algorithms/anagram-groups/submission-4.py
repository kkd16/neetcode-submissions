from string import ascii_lowercase

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        buckets = defaultdict(list)

        for s in strs:
            key = tuple(s.count(c) for c in ascii_lowercase)
            buckets[key].append(s)

        return list(buckets.values())
        