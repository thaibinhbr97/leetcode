# For both approaches
# Time: each recursion, make n! recursive calls (since n! permutations)
# for each, n operations (add to path and mark visited)
# O(n * n!) in total
# Space: recursive call stack: at most n levels deep and n! for result storage -> total is O(n * n!)

# def permute(nums):
#     def backtracking(nums, left, right):
#         if left == right:
#             ans.append(nums[:])
#             return
#         else:
#             for i in range(left, right):
#                 nums[i], nums[left] = nums[left], nums[i]
#                 backtracking(nums, left + 1, right)
#                 nums[i], nums[left] = nums[left], nums[i]

#     ans = []
#     backtracking(nums, 0, len(nums))
#     return ans


def permute(nums):
    def backtracking(path, visited):
        if len(path) == len(nums):
            ans.append(path[:])
            return

        for i in range(len(nums)):
            if visited[i]:  # skip used numbers
                continue
            visited[i] = True
            path.append(nums[i])
            backtracking(path, visited)  # recurse

            # backtrack
            path.pop()
            visited[i] = False

    ans = []
    backtracking([], [False] * len(nums))
    return ans


nums = [1, 2, 3]
print(
    permute(nums)
)  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


nums = [0, 1]
print(permute(nums))  # [[0, 1], [1, 0]]


nums = [1]
print(permute(nums))  # [[1]]
