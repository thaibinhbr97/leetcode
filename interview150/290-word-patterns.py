def wordPattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    char_to_word = {}
    word_to_char = {}
    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False  # pattern mismatch
        else:
            if word in word_to_char:
                return False  # word already mapped to another pattern
            char_to_word[char] = word
            word_to_char[word] = char
    return True


pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))  # true

pattern = "abba"
s = "dog cat cat fish"
print(wordPattern(pattern, s))  # false

pattern = "aaaa"
s = "dog cat cat dog"
print(wordPattern(pattern, s))  # false


pattern = "abba"
s = "dog dog dog dog"
print(wordPattern(pattern, s))  # false
