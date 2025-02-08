def squares(data):
    """DOCSTRING"""
    if len(data) == 0:
        return []
    
    else:
        return [(data[0])**2] + squares(data[1:])

print(squares([1, 13, 9, -11]))