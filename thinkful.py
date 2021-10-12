def fillable(stock, merch, n):
    # Your code goes here.
    
    if merch in stock:
        quantity = stock[merch]
        if n > quantity:
            return False
        elif n <= quantity:
            return True
    else:
        return False