class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0 
        vowels = "aeiou"
        count = 0
        max_count = 0
        for r in range(len(s)):

            if s[r] in vowels:
                count+=1

            if r-l+1 == k:
                max_count = max(max_count ,count )

                if s[l] in vowels:
                    count -=1
                
                l+=1    

        return max_count
