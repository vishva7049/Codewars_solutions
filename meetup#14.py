def order_food(lst): 
    #your code here
    # s1 = dict(lst)

    dic1 = {} 
    
    for dict in lst:
        if(dict['meal'] in dic1):
            dic1[dict['meal']] += 1
        else:
            dic1[dict['meal']] = 1
    return dic1