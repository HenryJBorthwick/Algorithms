def odds(data):
    if len(data) == 0:
        return []
    
    elif data[0] % 2 == 0:
        return odds(data[1:])
    
    else:
        return [data[0]] + odds(data[1:])
    
print(odds([0, 1, 12, 13, 14, 9, -11, -20]))