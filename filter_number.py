def filter_string(string):
    #your code here
    result = []

    for i in string:
        if i.isnumeric() == True:
            result.append(i)

    s1= ''.join(result)   
    return int(s1)

print(filter_string('dsbhjq2321fd'))