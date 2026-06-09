class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # loop thru array
        # store in a deque
        # store indexes
        # default to appending to the right, BUT keep it decreasing
        # so, when u got to add something to the deque, keep poppng till its decreasing again
        # grab max from [0] but clean it first

        q = collections.deque()
        res = []

        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            if r - l + 1 >= k:
                res.append(nums[q[0]])
                l += 1

            r += 1

        return res
