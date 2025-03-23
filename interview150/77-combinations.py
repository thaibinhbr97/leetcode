def combine(n, k):
    # Time: k * C(n,k) -> k*(n!/(k!(n-k)!)), k is the max recursion depth
    # Space: O(k) + (recursion depth) + O(C(n,k)) (storing results)
    def backtracking(n, k, combination, left):
        if k == 0:
            res.append(combination[:])
            return
        for i in range(left, n + 1):
            combination.append(i)
            backtracking(n, k - 1, combination, i + 1)
            combination.pop()

    res = []
    backtracking(n, k, [], 1)
    return res


n = 4
k = 2
print(combine(n, k))  # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]


n = 1
k = 1
print(combine(n, k))  # [[1]]
