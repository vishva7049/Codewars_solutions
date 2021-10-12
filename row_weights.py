def row_weights(array):
    t1 = [] # even
    t2 =[] # odd

    for i in range(0, len(array)):
        if i % 2:
            t1.append(array[i])
        else:
            t2.append(array[i])

    return (sum(t2) ,sum(t1))

print(row_weights([80]))
print(row_weights([5,23,24,2,23,42]))
