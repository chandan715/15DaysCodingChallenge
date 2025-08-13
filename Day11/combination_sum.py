class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def find_combinations(index, current, total):
            if total == target:
                result.append(current[:])
                return
            if total > target:
                return
            for i in range(index, len(candidates)):
                current.append(candidates[i]) 
                find_combinations(i, current, total + candidates[i])
                current.pop()
        find_combinations(0, [], 0)
        return result
            