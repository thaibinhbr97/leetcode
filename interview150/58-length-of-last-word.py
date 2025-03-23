def lengthOfLastWord(s):
    # Time: O(n)
    # Space: O(1)
    n = len(s)
    res = 0
    i = n - 1
    # ignore trailing spaces
    while i >= 0 and s[i] == " ":
        i -= 1
    # count length of last word
    while i >= 0 and s[i] != " ":
        i -= 1
        res += 1
    return res


s = "Hello World"
print(lengthOfLastWord(s))  # 5


s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))  # 4

s = "luffy is still joyboy"
print(lengthOfLastWord(s))  # 6

s = "word                "
print(lengthOfLastWord(s))  # 4
