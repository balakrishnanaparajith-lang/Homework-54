from functools import reduce

sentences = [
    "Python Is Amazing",
    "Map Filter Reduce Are Powerful",
    "I Love Coding"
]
def to_words(s):
    return s.lower().split()
lowered = list(map(to_words, sentences))
flattened = reduce(lambda a, b: a + b, lowered)
def check(w):
    return len(w) >= 4
filtered = list(filter(check, flattened))
def count(total, word):
    return total + len(word)
total_chars = reduce(count, filtered, 0)
print(total_chars)
