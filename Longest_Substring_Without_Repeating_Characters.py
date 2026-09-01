class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        hashmap = {}
        ans = 0
        l = 0

        for ch in range(len(s)):
            if s[ch] in hashmap and hashmap[s[ch]] >= l:
                l = hashmap[s[ch]] + 1

            hashmap[s[ch]] = ch
            ans = max(ans , ch-l+1)


        return ans