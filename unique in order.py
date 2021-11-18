def unique_in_order(iterable):
    # l1 = list(iterable)
    list1 = []
    char= "";
  #  print(iterable)
    for i in iterable:
        if(i != char):
            list1.append(i)
            char = i
    return list1
       

print(unique_in_order('AAAABBBCCDAABBB'))    