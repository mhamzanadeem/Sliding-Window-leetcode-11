class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Frequency map of characters we need to match (permutation of s1)
        need = Counter(s1)
        # Frequency map of characters in current window
        window = Counter()

        # Left pointer of sliding window
        l = 0

        # Right pointer expands the window
        for r in range(len(s2)):
            # Add current character to window
            window[s2[r]] += 1

            # If window size exceeds s1 length, shrink from left
            if r - l + 1 > len(s1):
                # Remove leftmost character from window
                window[s2[l]] -= 1

                # If character count reaches zero, remove from map entirely
                if window[s2[l]] == 0:
                    del window[s2[l]]

                # Move left pointer forward
                l += 1

            # If window matches target frequency map, permutation found
            if window == need:
                return True

        # No permutation of s1 found in s2
        return False