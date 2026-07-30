class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num]=1
        for key in map:
            if map[key] > 1:
                return True
        return False
        