def combinationSum(candidates, target):
    # def backtracking(path, left, curSum):
    #     if curSum == target:
    #         ans.append(path[:])
    #     elif curSum < target:
    #         for i in range(left, len(candidates)):
    #             path.append(candidates[i])
    #             backtracking(path, i, curSum + candidates[i])
    #             path.pop()

    # ans = []
    # backtracking([], 0, 0)
    # return ans

    # Time: O(N^(T/M)), N: # of elements in candidates, T: target value, M: smallest value in candidates
    # Space: O(T/M)
    def backtracking(path, left, remaining):
        if remaining == 0:
            ans.append(path[:])
            return
        if remaining < 0:
            return
        for i in range(left, len(candidates)):
            path.append(candidates[i])
            backtracking(path, i, remaining - candidates[i])
            path.pop()

    ans = []
    backtracking([], 0, target)
    return ans


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))  # [[2,2,3],[7]]

candidates = [2, 3, 5]
target = 8
print(combinationSum(candidates, target))  # [[2,2,2,2],[2,3,3],[3,5]]

candidates = [2]
target = 1
print(combinationSum(candidates, target))  # []
