class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        if len(s) < k:
            return False

        seen = set()

        for r in range(k-1, len(s)):
            window = s[r-k+1:r+1]
            seen.add(window)

            if len(seen) == 2 ** k:
                return True
            
        return False
