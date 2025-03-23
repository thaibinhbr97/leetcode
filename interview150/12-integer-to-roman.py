def intToRoman(num):
    # Time: O(1)
    # Space: O(1)
    roman_map = [
        (1, "I"),
        (4, "IV"),
        (5, "V"),
        (9, "IX"),
        (10, "X"),
        (40, "XL"),
        (50, "L"),
        (90, "XC"),
        (100, "C"),
        (400, "CD"),
        (500, "D"),
        (900, "CM"),
        (1000, "M"),
    ]
    # res = ""
    # for val, sym in reversed(roman_map):
    #     if num // val:
    #         count = num // val
    #         res += sym * count
    #         num = num % val
    # return res

    res = []
    for val, sym in reversed(roman_map):
        while num >= val:
            res.append(sym)
            num -= val
    return "".join(res)


num = 3749
print(intToRoman(num))  # MMMDCCXLIX

num = 58
print(intToRoman(num))  # LVIII

num = 1994
print(intToRoman(num))  # MCMXCIV
