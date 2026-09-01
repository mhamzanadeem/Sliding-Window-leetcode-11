class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Edge case: if k <= 1, no positive product can be less than k
        if k <= 1:
            return 0
        
        # Count of valid subarrays
        ans = 0
        # Running product of current window
        prod = 1
        # Left pointer of sliding window
        left = 0
        
        # Right pointer expands the window with value
        for right, val in enumerate(nums):
            # Multiply current value into product
            prod *= val
            
            # Shrink window from left while product is too large
            while prod >= k and left <= right:
                # Divide out the leftmost element
                prod //= nums[left]
                # Move left pointer forward
                left += 1
            
            # All subarrays ending at right with start in [left, right] are valid
            # Count = right - left + 1
            ans += right - left + 1
        
        return ans