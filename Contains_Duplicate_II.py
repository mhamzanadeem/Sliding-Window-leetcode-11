class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        result = set()

        left = 0 
        for right in range(len(nums)):
            if right - left > k:
                result.remove(nums[left])
                left +=1
            if nums[right] in result:
                return True
            result.add(nums[right])
        
        return False