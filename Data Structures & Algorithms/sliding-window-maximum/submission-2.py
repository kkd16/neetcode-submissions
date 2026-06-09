class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # loop thru array
        # store in a deque
        # store indexes
        # default to appending to the right, BUT keep it decreasing
        # so, when u got to add something to the deque, keep poppng till its decreasing again
        # grab max from [0] but clean it first

        d = collections.deque()

        res = []

        for i in range(k):
            while d and nums[d[-1]] < nums[i]:
                d.pop()
            d.append(i)

        res.append(nums[d[0]])

        for i in range(k, len(nums)):

            while len(d) > 0 and nums[d[-1]] < nums[i]:
                d.pop()
            
            d.append(i)

            while d[0] <= i - k:
                d.popleft()

            res.append(nums[d[0]])

        return res
