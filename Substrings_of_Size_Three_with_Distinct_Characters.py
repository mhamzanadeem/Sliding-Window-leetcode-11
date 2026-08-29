class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0

        for r in range(2,len(s)):
            if len(set(s[r-2:r+1])) == 3:
                count +=1
        
        return count