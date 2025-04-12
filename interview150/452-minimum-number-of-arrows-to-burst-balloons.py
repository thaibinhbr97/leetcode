def findMinArrowShots(points: list[list[int]]) -> int:
    """
    sort by end point
    track the last arrow shot (end)
    only increment when the next balloon's start is after the end
    time: O(nlogn)
    space: O(1)
    """
    # if not points:
    #     return 0
    # points.sort(key=lambda x: x[1])
    # res = 1
    # n = len(points)
    # end = points[0][1]
    # for i in range(1, n):
    #     if points[i][0] > end:
    #         res += 1
    #         end = points[i][1]
    # return res

    """
    time: O(nlogn)
    space: O(1)
    """
    if not points:
        return 0
    points.sort()
    n = len(points)
    res = n
    prev = points[0]
    for i in range(1, n):
        curr = points[i]
        if curr[0] <= prev[1]:
            res -= 1
            prev = [curr[0], min(curr[1], prev[1])]
        else:
            prev = curr
    return res


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
test_points = [[1, 6], [2, 8], [7, 12], [10, 16]]
print(findMinArrowShots(points))  # 2

points = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(findMinArrowShots(points))  # 4


points = [[1, 2], [2, 3], [3, 4], [4, 5]]
print(findMinArrowShots(points))  # 2

points = [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]
print(findMinArrowShots(points))  # 2
