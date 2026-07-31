class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        glbMap = {}
        for currWord in strs:
            word = ''.join(sorted(currWord))
            if word not in glbMap:
                glbMap[word] = []

            glbMap[word].append(currWord)
        res = []
        for x in glbMap:
            res.append(glbMap[x])
        return res

        