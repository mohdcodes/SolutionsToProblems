class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = set(nums)
        maxCount = 0
        for num in nums:
            if num-1 not in nums:
                curr = num
                count = 1
                while curr+1 in nums:
                    count += 1
                    curr += 1 
                maxCount = max(count, maxCount)
        return maxCount