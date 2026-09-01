class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Deque to store indices of elements in decreasing order of values
        q = deque()
        # Result list to store maximum of each window
        result = []

        # Right pointer expands the window
        for r in range(len(nums)):

            # Remove indices from front that are outside current window
            while q and q[0] < r - k + 1:
                q.popleft()

   
            # Remove indices from back whose values are smaller than current
            # (they can never be the maximum while current element is in window)
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # Add current index to deque
            q.append(r)

            # Once window reaches size k, record the maximum (front of deque)
            if r >= k - 1:
                result.append(nums[q[0]])

        return result