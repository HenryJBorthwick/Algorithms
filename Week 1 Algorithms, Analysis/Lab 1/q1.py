def concat_list(strings):
    """ list of strings as a parameter and returns a single string made up of all the individual strings in strings concatenated together, in order"""
    if len(strings) == 0:
        return ""
    else:
        return strings[0] + concat_list(strings[1:])

ans = concat_list(['a', 'hot', 'day'])
print(ans)   

ans = concat_list(['x', 'y', 'z'])
print(ans)

print(concat_list([]))