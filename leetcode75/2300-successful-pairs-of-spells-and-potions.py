def successfulPairs(spells, potions, success):
    # Time: O(mlogm + nlogn), m: length of potions, n: length of spells, each spell requires binary search on sorted potions
    # Space: O(n) for storing results
    potions.sort()
    n = len(potions)
    res = []

    def countSuccess(spell, potions, success):
        low = 0
        high = n - 1
        minStrength = success / spell
        while low <= high:
            mid = (low + high) // 2
            strength = potions[mid]
            if strength < minStrength:
                low = mid + 1
            else:
                high = mid - 1
        count = n - low
        return count

    for spell in spells:
        count = countSuccess(spell, potions, success)
        res.append(count)

    return res


"""
7: success
5: spell
1.4
[1,2,3,4,5]
"""
