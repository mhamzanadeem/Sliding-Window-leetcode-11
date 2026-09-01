class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # Count of good substrings (all 3 characters distinct)
        count = 0

        # Fixed-size window of 3: start from index 2
        for r in range(2,len(s)):
            # Check if the 3-character window has all distinct characters
            if len(set(s[r-2:r+1])) == 3:
                count +=1
        
        return count