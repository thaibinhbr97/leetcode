"""
Decode String

k[encoded_string] -> encoded_string * k

3[a]2[bc] -> aaabcbc
3[a2[c]] -> accaccacc
2[abc]3[cd]ef -> abcabccdcdcdef
"""


def decodeString(s):
    stack = []
    for c in s:
        if c != "]":
            stack.append(c)
        else:
            substr = ""
            while stack[-1] != "[":
                substr = stack.pop() + substr
            stack.pop()  # pop opening bracket [
            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            stack.append(int(k) * substr)
    return "".join(stack)


s = "3[a]2[bc]"
print(decodeString(s))  # aaabcbc
s = "3[a2[c]]"
print(decodeString(s))  # accaccacc
s = "2[abc]3[cd]ef"
print(decodeString(s))  # abcabccdcdcdef
