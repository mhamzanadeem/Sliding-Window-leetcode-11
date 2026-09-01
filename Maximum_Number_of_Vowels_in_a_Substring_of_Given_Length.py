class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Left pointer of sliding window
        l = 0 
        # String of vowels for quick lookup
        vowels = "aeiou"
        # Count of vowels in current window
        count = 0
        # Maximum vowel count found
        max_count = 0
        # Right pointer expands the window
        for r in range(len(s)):

            # If current character is a vowel, increment count
            if s[r] in vowels:
                count+=1

            # When window reaches size k
            if r-l+1 == k:
                # Update max_count if current window has more vowels
                max_count = max(max_count ,count )

                # If leftmost character is a vowel, decrement count (leaving window)
                if s[l] in vowels:
                    count -=1
                
                # Move left pointer forward (slide window)
                l+=1    

        return max_count