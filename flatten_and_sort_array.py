def flatten_and_sort(array):
    
    l1 = []

    for i in array:
        for j in i:
            l1.append(j)
    return sorted(l1)