def valid_phone_number(phone_number):
    comparator = {
    0 : "(",
    4: ")",
    5: " ",
    9: "-",
    14: ")"
    }
    
    if(len(phone_number) != 14):
        return False

    for i in range(0,len(phone_number)):
        if(i in comparator):
            if(phone_number[i] == comparator[i]):
                continue
            else:
                return False
        else:
            if(phone_number[i].isdigit()):
                continue
            else:
                return False
    return True