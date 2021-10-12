def sort_array(source_array):
    # Return a sorted array.
    index = []
    numbers = []

    for i in range(0,len(source_array)):
        if(source_array[i]%2 != 0):
          index.append(i)
          numbers.append(source_array[i])

    numbers.sort()
 
    for i in range(0,len(numbers)):
        source_array[index[i]] = numbers[i]

    return source_array