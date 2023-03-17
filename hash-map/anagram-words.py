from collections import defaultdict
def dict_builder(word):
    a = defaultdict(int)
    for char in word:
        a[char] += 1
    return a
def is_anagram(word1: str, word2: str) -> bool:
    counter = dict_builder(word1)
    for char in word2:
        counter[char] -= 1
    return all(n == 0 for n in counter.values())
