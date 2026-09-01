class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Edge case: empty string or single character
        if len(s) < 2:
            return len(s)
        
        # Hash map to store last seen index of each character
        hashmap = {}
        # Store the maximum length found
        ans = 0
        # Left pointer of sliding window
        l = 0

        # Right pointer expands the window by iterating through string
        for ch in range(len(s)):
            # If character exists in map and is within current window
            if s[ch] in hashmap and hashmap[s[ch]] >= l:
                # Move left pointer to avoid duplicate
                l = hashmap[s[ch]] + 1

            # Update last seen index of current character
            hashmap[s[ch]] = ch
            # Update maximum length with current window size
            ans = max(ans , ch-l+1)


        return ans