def move_zeros(array):
    zeros= []
    new = []
    for i in range(len(array)):
        if array[i] == 0:
            zeros.append(array[i])

        else:
          new.append(array[i])

    return new +  zeros

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
