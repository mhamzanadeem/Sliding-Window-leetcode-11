class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        # Edge case: if string is shorter than k, impossible to have all codes
        if len(s) < k:
            return False

        # Set to store all unique binary substrings of size k we've seen
        seen = set()

        # Fixed-size window: slide from index k-1 to end of string
        for r in range(k-1, len(s)):
            # Extract the current window of size k
            window = s[r-k+1:r+1]
            # Add the binary substring to our set
            seen.add(window)

            # Early exit: if we've seen all 2^k possible codes, return True
            if len(seen) == 2 ** k:
                return True
            
        # If we finished scanning and didn't find all codes, return False
        return False