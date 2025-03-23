def jump(nums):
    # Time: O(n)
    # Space: O(1)
    n = len(nums)
    max_reach = 0
    cur_end = 0
    steps = 0
    for i in range(
        n - 1
    ):  # don't need to traverse to the index since cur_end will consider the last jump from max_reach assignment
        max_reach = max(max_reach, i + nums[i])
        if i == cur_end:
            steps += 1
            cur_end = max_reach
            if cur_end >= n - 1:  # stop if we reach last index
                break
    return steps


nums = [2, 3, 1, 1, 4]
print(jump(nums))  # 2

nums = [2, 3, 0, 1, 4]
print(jump(nums))  # 2
