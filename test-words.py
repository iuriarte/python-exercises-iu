def word_histogram(word):
    words = ""
    word_list = []
    word_lib = {}
    for i in range(len(word)):
        print(word_list)
        if word[i] == " ":
            word_list.append(words)
            #print(word_list)
            words = ""
            #print(words)
        #print(word_list)
        elif i == len(word)-1:
            print(word_list)
            words = words + word[i]
            word_list.append(words)

        else:
            words = words + word[i]

    for j in range(len(word_list)):
        word_lib[word_list[j]] = word_lib.get(word_list[j],0)
        word_lib[word_list[j]] = word_lib[word_list[j]] + 1
    print(word_lib)
word_histogram('to be or not to be')