

def inverse_slice(items, a, b):
    # Your code here.
    newList = []
    for i in range(0,len(items)):
        if(i < a or i >= b):
            newList.append(items[i])
    return newList