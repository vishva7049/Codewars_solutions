def count_positives_sum_negatives(arr):
    #list1 = []
    #list2 = []
    newarr = [0,0]

    if(arr == None or len(arr)==0):
            return arr
    for i in arr:        
        if i>= 1:
            newarr[0] = newarr[0]+1         
        else:
            newarr[1] = newarr[1] + i
    return newarr


print(count_positives_sum_negatives([22,33,2,-1,-2,-1]))