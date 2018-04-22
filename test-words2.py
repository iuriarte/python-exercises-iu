def word_histogram(sentence):
    word_list = sentence.split()
    print("wordl_list: ", word_list)
    word_lib = {}
    print("word_lib: ",word_lib)
    for word in word_list:
        if word not in word_lib:
            word_lib[word] = 1
            print("word_lib[word]: ",word_lib[word])
            print("word_lib: ", word_lib)
        else:
            word_lib[word] += 1
            print(word_lib[word])
            print(word_lib)
    print(word_lib)
word_histogram('to be or not to be')