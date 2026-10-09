class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] # T: O(2^t , t == target)
        candidates.sort()

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return 
            if i >= len(candidates) or total > target:
                return 
            
            #including the candidates[i]
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])
            
            #not including the candidates[i]
            curr.pop()# removing the candidates[i]
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return res
