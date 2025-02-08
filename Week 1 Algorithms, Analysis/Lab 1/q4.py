def odds(data):
    """Docstring"""
    if len(data) == 0:
        return [] 

    #RETURN ODD NUMBER
    elif data[0] % 2 == 1: #Odd
        return [data[0]] + odds(data[1:])

    else:
        return odds(data[1:])

print(odds([0, 1, 12, 13, 14, 9, -11, -20]))
