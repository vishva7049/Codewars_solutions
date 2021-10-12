def last_survivor(letters, coords): 
    # your code here
    # use for loop to iterate over array
    for i in coords:
        arr1 = list(letters)
        arr1.pop(i)
        letters = ''.join(arr1)
    
    return letters
        
    # use element from array and remove the element from string that matches with array element.
    
