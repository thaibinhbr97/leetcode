def strStr(haystack, needle):
    n = len(haystack)
    m = len(needle)
    if m == 0:
        return 0  # empty needle
    i = 0
    j = 0
    while i < n:
        if haystack[i] == needle[j]:  # if both pointers match, move two pointers
            j += 1
            if j == m:
                return i - j + 1
        else:
            i -= j  # reset i back to next start position
            j = 0
        i += 1
    return -1  # no match found


haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))  # 0

haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))  # -1

haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))  # 2
