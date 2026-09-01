class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # Left pointer of sliding window
        l = 0
        # Running sum of current window elements
        current_sum = 0
        # Track the maximum sum found (initialized to negative infinity)
        max_sum = float("-inf")
       
        # Right pointer expands the window
        for r in range(len(nums)):
            # Add current element to window sum
            current_sum += nums[r]

            # When window reaches size k
            if r-l+1 ==k:

                # Update max_sum if current window sum is larger
                max_sum = max(max_sum , current_sum)
                # Remove leftmost element from sum (slide window)
                current_sum -= nums[l]
                # Move left pointer forward
                l+=1

        # Return maximum average (sum divided by k)
        return max_sum/k