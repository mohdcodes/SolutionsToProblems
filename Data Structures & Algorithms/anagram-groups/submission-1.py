class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # glbMap = {}
        # for currWord in strs:
        #    word = ''.join(sorted(currWord))
        #    if word not in glbMap:
        #        glbMap[word] = []

        #    glbMap[word].append(currWord)
        # res = []
        # for x in glbMap:
        #    res.append(glbMap[x])
        # return res

        glbMap = defaultdict(list)
        for word in strs:
            count = [0]*26
            # frequency mapping
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            glbMap[tuple(count)].append(word)
        res = []
        return list(glbMap.values())

        