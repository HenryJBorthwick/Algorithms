def my_enumerate(items, index=0):
    """DOCSTRING"""
    if len(items) == index:
        return []
    else:
        return [(index, items[index])] + my_enumerate(items, index+1)
    
ans = my_enumerate([10, 20, 30])
print(ans)

ans = my_enumerate(['dog', 'pig', 'cow'])
print(ans)

ans = my_enumerate([])
print(ans)