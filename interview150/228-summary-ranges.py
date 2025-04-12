def summaryRanges(nums):
    # Time: O(n)
    # Space: O(1)
    n = len(nums)
    if n == 0:
        return []
    if n == 1:
        return [str(nums[0])]
    left = 0
    res = []
    for right in range(1, n + 1):
        if right == n or nums[right] - nums[right - 1] != 1:
            if left == right - 1:
                res.append(str(nums[left]))
            else:
                res.append(f"{nums[left]}->{nums[right-1]}")
            left = right
    return res


nums = [0, 1, 2, 4, 5, 7]
#                l
#                      r
# temp "0->2"
# res ["0->2", "4->5"]
print(summaryRanges(nums))  # ["0->2","4->5","7"]

nums = [0, 2, 3, 4, 6, 8, 9]
print(summaryRanges(nums))  # ["0","2->4","6","8->9"]
