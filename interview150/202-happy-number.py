def isHappy(n):
    # Time: O(logn)
    # Space: O(logn)
    def get_sum(n):
        total = 0
        while n > 0:
            last_digit = n % 10
            total += last_digit**2
            n //= 10
        return total

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_sum(n)
    return n == 1


n = 19
print(isHappy(n))  # true

n = 2
print(isHappy(n))  # false
