def recursive_divide(x, y):
    """DOCSTING"""
    #See how many times you can subtract a particular number from the other
    #As it gets smaller 
    if x <= y:
        return 0
    else:
        return 1 + recursive_divide(x - y, y)
    
print(recursive_divide(8, 3))
print(recursive_divide(9, 3))


