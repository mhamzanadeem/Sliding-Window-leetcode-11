class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Frequency map for characters in current window
        count = {}
        # Track the most frequent character count in current window
        max_freq = 0
        # Left pointer of sliding window
        left = 0
        # Store the maximum valid window length found
        max_length = 0
        
        # Right pointer expands the window
        for right in range(len(s)):
            # Add current character to frequency map
            count[s[right]] = count.get(s[right], 0) + 1
            # Update the maximum frequency seen so far
            max_freq = max(max_freq, count[s[right]])
            
            # Window size minus max_freq = characters needing replacement
            # If this exceeds k, window is invalid, shrink from left
            while (right - left + 1) - max_freq > k:
                # Remove left character from frequency map
                count[s[left]] -= 1
                # Move left pointer forward
                left += 1
                # Recalculate max_freq after shrinking (optimization needed)
                max_freq = max(count.values())
            
            # Update maximum length with current valid window size
            max_length = max(max_length, right - left + 1)
        
        return max_length