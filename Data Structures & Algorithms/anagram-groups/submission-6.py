class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # loop str in strs
        # count all letters in str
        # there are 26 letters, so make an array of size 26, where 
        # index of array = index in alphabet, value = count of that letter
        # group into sets of count objects
        # convert sets into array


        groups = collections.defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                counts[idx] += 1

            groups[tuple(counts)].append(s)

        return list(groups.values())     