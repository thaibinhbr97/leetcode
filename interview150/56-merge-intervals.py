def merge(intervals):
    # sort intervals from low to high
    # idea: if second element of the interval is larger than or equal to the first elements in a sorted list of intervals
    # which means that it can be merged. Otherwise, it cannot be merged.
    # We can use two pointer approach to look at the current interval and the next interval and make a
    # comparison. If 2nd element of cur inter >= than 1st element of next inter, move the right pointer to check
    # the one after that if it satisfied the above condition or not.
    # If it is, continue moving the right pointer. If not, use the 1st element of left inter and 2nd element of
    # the right inter to merge and append to the res.
    # Time: O(nlogn), through sorting intervals
    # Space: O(n), length of res, in the worst case senerio it takes all of the non-merged intervals to the res
    # intervals.sort()
    # n = len(intervals)
    # left = 0
    # right = 1
    # res = []
    # while right <= n:
    #     # continue moving right while intervals overlap
    #     while right < n and intervals[right][0] <= intervals[right - 1][1]:
    #         intervals[right][0] = intervals[left][
    #             0
    #         ]  # update current start to the leftmost start
    #         intervals[right][1] = max(
    #             intervals[right][1], intervals[right - 1][1]
    #         )  # merge
    #         right += 1
    #     # append merged interval
    #     res.append([intervals[left][0], intervals[right - 1][1]])
    #     left = right
    #     right += 1
    # return res

    # Time: O(logn)
    # Space: O(n)
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # overlap occurs
            last[1] = max(last[1], current[1])  # merge
        else:
            merged.append(current)
    return merged


def test_merge():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    res = [[1, 6], [8, 10], [15, 18]]
    print(merge(intervals) == res)
    print(merge(intervals))

    intervals = [[1, 4], [4, 5]]
    res = [[1, 5]]
    print(merge(intervals) == res)
    print(merge(intervals))


test_merge()
