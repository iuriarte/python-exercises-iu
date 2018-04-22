import collections
word = str(input('letter_histogram: '))
word_array = []
unique = []
counter = collections.Counter()
def letter_histogram(word):
    for char in word:
        word_array.append(char)
        print(word_array)
    counter.update(word_array)
    return word_array

histogram = set(letter_histogram(word))

print(histogram)
print(counter)

