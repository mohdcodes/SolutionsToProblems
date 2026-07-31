class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        map = {}
        res = []
        for num in nums:
            map[num] = map.get(num, 0) + 1
        freqMap = sorted(nums, key=lambda x :(map[x], -x))
        print(freqMap)
        rev = freqMap[::-1]
        print(rev)
        c = 0
        i = 1
        while k:
            while c<len(rev) and rev[i] == rev[c]:
                c += 1
            res.append(rev[i])
            i = c
            k-=1
        return res
        