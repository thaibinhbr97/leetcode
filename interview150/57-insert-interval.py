def insert(intervals, newInterval):
    # # time: O(n)
    # # space: O(n)
    # if not intervals:
    #     return [newInterval]
    # res = []
    # i = 0
    # n = len(intervals)
    # # add all intervals before newInterval
    # while i < n and intervals[i][1] < newInterval[0]:
    #     res.append(intervals[i])
    #     i += 1
    # # merge overlapping intervals with newInterval
    # # condition for merging intervals[i][0] <= newInterval[1]
    # while i < n and intervals[i][0] <= newInterval[1]:
    #     newInterval[0] = min(intervals[i][0], newInterval[0])
    #     newInterval[1] = max(intervals[i][1], newInterval[1])
    #     i += 1
    # res.append(newInterval)

    # # add all intervals after newInterval
    # while i < n:
    #     res.append(intervals[i])
    #     i += 1
    # return res

    # time: O(n)
    # space: O(1)
    # in-place
    if not intervals:
        return [newInterval]
    i = 0
    n = len(intervals)
    # add all intervals before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        i += 1
    # merge overlapping intervals with newInterval
    # condition for merging intervals[i][0] <= newInterval[1]
    start = i
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(intervals[i][0], newInterval[0])
        newInterval[1] = max(intervals[i][1], newInterval[1])
        i += 1
    intervals[start:i] = [newInterval]
    return intervals

    # time: O(n)
    # space: O(n)
    # res = []
    # n = len(intervals)
    # for i in range(n):
    #     if intervals[i][1] < newInterval[0]:
    #         res.append(intervals[i])
    #     elif intervals[i][0] > newInterval[1]:
    #         res.append(newInterval)
    #         return res + intervals[i:]
    #     else:
    #         newInterval[0] = min(newInterval[0], intervals[i][0])
    #         newInterval[1] = max(newInterval[1], intervals[i][1])
    # res.append(newInterval)
    # return res

    # time: O(nlogn)
    # space: O(n)
    # if not intervals:
    #     return [newInterval]
    # intervals.append(newInterval)
    # intervals.sort()
    # merged = [intervals[0]]
    # for current in intervals[1:]:
    #     last = merged[-1]
    #     if current[0] <= last[1]:  # overlap occurs
    #         last[1] = max(last[1], current[1])
    #     else:
    #         merged.append(current)
    # return merged


def test_insert():
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(insert(intervals, newInterval) == [[1, 5], [6, 9]])
    print(insert(intervals, newInterval))

    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(insert(intervals, newInterval) == [[1, 2], [3, 10], [12, 16]])
    print(insert(intervals, newInterval))


test_insert()
