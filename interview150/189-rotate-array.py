def rorateArray(nums, k):
    # Time: O(n), n is length of nuns
    # Space: O(n)
    # n = len(nums)
    # k = k % n  # handle case where k > n
    # temp = [0] * n
    # for i in range(n):
    #     temp[(i + k) % n] = nums[i]
    # nums[:] = temp

    # # Time: O(n)
    # # Space: O(n)
    # n = len(nums)
    # temp = nums[:]
    # k = k % n
    # # reverse nums array
    # temp = temp[::-1]
    # # reverse 0 -> k and reverse k + 1 -> n
    # temp = temp[:k][::-1] + temp[k:][::-1]
    # nums[:] = temp

    # # Time: O(n)
    # # Space: O(1)
    # n = len(nums)
    # k = k % n

    # def reverse(start, end):
    #     while start < end:
    #         nums[start], nums[end] = nums[end], nums[start]
    #         start += 1
    #         end -= 1

    # reverse(0, n - 1)
    # reverse(0, k - 1)
    # reverse(k, n - 1)

    # Time: O(n)
    # Space: O(1)
    n = len(nums)
    k = k % n  # handle k > n
    start = 0
    count = 0  # track number of swaps

    while count < n:
        curr = start
        prev = nums[start]
        while True:
            next_idx = (curr + k) % n
            nums[next_idx], prev = prev, nums[next_idx]
            curr = next_idx
            count += 1
            if start == curr:
                break
        start += 1


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rorateArray(nums, k)  # [5,6,7,1,2,3,4]

nums = [-1, -100, 3, 99]
k = 2
rorateArray(nums, k)  # [3, 99, -1, -100]
