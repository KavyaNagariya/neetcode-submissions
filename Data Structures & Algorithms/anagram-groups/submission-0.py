class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 
        for word in strs:
            sortedS = ''.join(sorted(word))
            res[sortedS].append(word)
        return list(res.values())