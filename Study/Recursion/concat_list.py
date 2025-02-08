def concat_list(strings):
    if len(strings) == 0:
        return ""
    
    else:
        return strings[0] + concat_list(strings[1:])
    

ans = concat_list(['a', 'hot', 'day'])
print(ans)

ans = concat_list(['x', 'y', 'z'])
print(ans)

print(concat_list([]))