import collections

paragraph = str(input('word_histogram: '))
paragraph_dictionary = dict()
word_array = []
unique = []
counter = collections.Counter()
def word_histogram(paragraph):
    for word in paragraph.items():
        word_array[word]=paragraph_dictionary.get(word)
        print(word_array)
    counter.update(word_array)
    return word_array

histogram = set(word_histogram(paragraph))

print(histogram)
print(counter)

