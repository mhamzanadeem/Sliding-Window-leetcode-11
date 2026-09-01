class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: empty input strings
        if not s or not t:
            return ""
        
        # Build frequency map of characters we need to find
        target_count = {}
        for char in t:
            target_count[char] = target_count.get(char, 0) + 1
        
        # Number of unique characters we need to match
        required = len(target_count)
        

        # Left pointer of sliding window
        left = 0
        # Right pointer expands the window
        right = 0
        # Count of unique chars with required frequency in window
        formed = 0  
        # Frequency map of characters in current window
        window_count = {}
        
        # Track minimum window length found
        min_length = float('inf')
        # Track starting index of minimum window
        min_left = 0
        
        # Expand window by moving right pointer
        while right < len(s):
            # Character at right pointer
            char = s[right]
            # Add character to window frequency map
            window_count[char] = window_count.get(char, 0) + 1
            
            # Check if this character's frequency meets the requirement
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1
            
            # Try to shrink window while all requirements are met
            while left <= right and formed == required:
                # Character at left pointer (about to leave window)
                char_left = s[left]
                
                # Update minimum window if current is smaller
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_left = left
                
                # Remove left character from window count
                window_count[char_left] -= 1
                # If this character no longer meets requirement, decrement formed
                if char_left in target_count and window_count[char_left] < target_count[char_left]:
                    formed -= 1
                
                # Move left pointer to try shrinking further
                left += 1
            
            # Expand window to the right
            right += 1
        
        # Return minimum window substring, or empty string if none found
        return "" if min_length == float('inf') else s[min_left:min_left + min_length]