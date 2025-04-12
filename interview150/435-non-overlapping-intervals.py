def eraseOverLapIntervals(intervals: list[list[int]]) -> int:
    # time: O(nlog)
    # space: O(1)
    if not intervals:
        return 0
    # sort by end time
    intervals.sort(key=lambda x: x[1])
    end = intervals[0][1]
    res = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:  # overlapping occurs, remove current interval
            res += 1
        else:
            end = intervals[i][1]  # no overlap, update end time
    return res


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(eraseOverLapIntervals(intervals))  # 1

intervals = [[1, 2], [1, 2], [1, 2]]
print(eraseOverLapIntervals(intervals))  # 2

intervals = [[1, 2], [2, 3]]
print(eraseOverLapIntervals(intervals))  # 0

intervals = [
    [-52, 31],
    [-73, -26],
    [82, 97],
    [-65, -11],
    [-62, -49],
    [95, 99],
    [58, 95],
    [-31, 49],
    [66, 98],
    [-63, 2],
    [30, 47],
    [-40, -26],
]
print(eraseOverLapIntervals(intervals))  # 7


intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
print(eraseOverLapIntervals(intervals))  #
