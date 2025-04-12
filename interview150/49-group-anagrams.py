def groupAnagrams(strs):
    """
    anagrams <=> sorting words
    time: O()
    """
    words_map = {}
    res = []
    for str in strs:
        # sort str and use words_map to keep track of key values pair. Key as sorted_str and values are arrays of str.
        sorted_str = "".join(sorted(str))
        if sorted_str not in words_map:
            words_map[sorted_str] = [str]
        else:
            words_map[sorted_str].append(str)
    for v in words_map.values():
        res.append(v)
    return res


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))  # [["bat"],["nat","tan"],["ate","eat","tea"]]

strs = [""]
print(groupAnagrams(strs))  # [[""]]

strs = ["a"]
print(groupAnagrams(strs))  # [["a"]]
