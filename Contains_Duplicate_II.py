class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Set to track elements currently in our sliding window
        result = set()

        # Left pointer of our sliding window
        left = 0 
        # Right pointer expands the window by iterating through array
        for right in range(len(nums)):
            # If window size exceeds k, shrink from left
            if right - left > k:
                # Remove the element leaving the window
                result.remove(nums[left])
                # Move left pointer forward
                left +=1
            # Check if current element already exists in window (duplicate found)
            if nums[right] in result:
                return True
            # Add current element to the window
            result.add(nums[right])
        
        # No nearby duplicates found
        return False