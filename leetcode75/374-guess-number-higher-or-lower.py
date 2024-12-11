def guessNumber(n):
    low = 1
    high = n
    while low <= high:
        mid = (low + high) // 2
        trial = guess(mid)
        if trial == 0:
            return trial
        elif trial == 1:
            low = mid + 1
        else:
            high = mid - 1


n = 10
pick = 6
print(guessNumber(n))

n = 1
pick = 1
print(guessNumber(n))

n = 2
pick = 1
print(guessNumber(n))
