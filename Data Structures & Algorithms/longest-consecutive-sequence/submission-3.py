class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0  # Fix 1: Handle empty input
        
        # Fix 2: Remove duplicates FIRST, then sort
        nums = sorted(list(set(nums))) 
        
        count = 1
        maxCount = 1  # Fix 3: Default to 1 if elements exist
        
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                count += 1
                maxCount = max(count, maxCount)
            else:
                count = 1
                
        return maxCount
