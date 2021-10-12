def spin_words(sentence):
    # Your code goes here
    reverse = []
    x = sentence.split()

    for i in x:
        if len(i) >= 5:
            reverse.append(i[::-1])

        else:
            reverse.append(i)


    return " ".join(reverse)