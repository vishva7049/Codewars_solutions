def remove_duplicate_words(s):
    a= s.split();
    list1 = []

    for i in a:
        if i not in list1:
            list1.append(i)

    return (" ".join(list1))