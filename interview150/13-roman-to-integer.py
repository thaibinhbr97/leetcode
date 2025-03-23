def romanToInt(s):
    # Time: O(n)
    # Space: O(n)
    # mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    # stack = []
    # for letter in s:
    #     stack.append(letter)
    # integer = 0
    # while stack:
    #     letter = stack.pop()
    #     if stack:
    #         top = stack[-1]
    #     else:
    #         top = ""
    #     if letter in ("V", "X"):
    #         integer += mapping[letter]
    #         if top == "I":
    #             integer -= mapping[top]
    #             stack.pop()
    #     elif letter in ("L", "C"):
    #         integer += mapping[letter]
    #         if top == "X":
    #             integer -= mapping[top]
    #             stack.pop()
    #     elif letter in ("D", "M"):
    #         integer += mapping[letter]
    #         if top == "C":
    #             integer -= mapping[top]
    #             stack.pop()
    #     else:
    #         integer += mapping[letter]
    # return integer

    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev_value = 0
    for char in reversed(s):
        curr_value = roman_map[char]
        if curr_value >= prev_value:
            total += curr_value
        else:
            total -= curr_value
        prev_value = curr_value
    return total


s = "IV"
print(romanToInt(s))  # 4

s = "VI"
print(romanToInt(s))  # 6

s = "LVIII"
print(romanToInt(s))  # 58

s = "MCMXCIV"
print(romanToInt(s))  # 1994
