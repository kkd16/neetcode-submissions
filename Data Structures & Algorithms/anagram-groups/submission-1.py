class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        lists = {}

        for s in strs:

            bucket = [0] * 26
            for c in s:
                bucket[ord(c) - ord('a')] += 1

            if tuple(bucket) not in lists:
                lists[tuple(bucket)] = [s]
            else:
                lists[tuple(bucket)].append(s)

        return list(lists.values())


        