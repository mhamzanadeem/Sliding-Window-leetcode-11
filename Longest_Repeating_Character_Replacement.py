class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            
            # Shrink window if invalid
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                # Recalculate max_freq after shrinking
                max_freq = max(count.values())
            
            max_length = max(max_length, right - left + 1)
        
        return max_length