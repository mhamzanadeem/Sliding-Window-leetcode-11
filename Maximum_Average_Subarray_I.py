

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        l = 0
        current_sum = 0
        max_sum = float("-inf")
       
        for r in range(len(nums)):
            current_sum += nums[r]

            if r-l+1 ==k:

                max_sum = max(max_sum , current_sum)
                current_sum -= nums[l]
                l+=1

        return max_sum/k


