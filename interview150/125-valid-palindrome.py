def isPalindrome(s):
    # Time: O(n)
    # Space: O(1)
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            return False
    return True


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))  # true

s = "race a car"
print(isPalindrome(s))  # false

s = " "
print(isPalindrome(s))  # true
