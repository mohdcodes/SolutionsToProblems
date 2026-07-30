class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}
        # base condition 1
        if len(s) != len(t):
            return False
        for char in range(len(s)):
            if s[char] in mapS:
                mapS[s[char]] += 1
            else:
                mapS[s[char]]= 1
        print(mapS)
        for char in range(len(t)):
            if t[char] in mapT:
                mapT[t[char]]+= 1
            else:
                mapT[t[char]]= 1
        print(mapT)
        return mapS == mapT
