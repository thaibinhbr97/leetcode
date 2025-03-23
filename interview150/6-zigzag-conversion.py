def convert(s, numRows):
    # Time: O(n), n is length of s
    # Space: O(m), m is length of numRows
    n = len(s)
    if numRows == 1 or numRows >= n:
        return s
    res = ["" for i in range(numRows)]
    i = 0
    shift = 1
    for char in s:
        res[i] += char
        if i == 0:
            shift = 1
        elif i == numRows - 1:
            shift = -1
        i += shift
    return "".join(res)


s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))  # "PAHNAPLSIIGYIR"


s = "PAYPALISHIRING"
numRows = 4
print(convert(s, numRows))  # "PINALSIGYAHRPI"

s = "A"
numRows = 1
print(convert(s, numRows))  # "A"
