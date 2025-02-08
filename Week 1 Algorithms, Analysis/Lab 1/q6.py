def find(data, value):
    """REUTRN INDEX OF FIRST OCCURENCE"""
    #PRECHECK
    if value not in data:
        return None

    #IF LIST IS EMPTY OR REACH END
    if len(data) == 0:
        return 0

    #Check if target, Return Postion(index) of target WITHOUT using index
    elif data[0] == value:
        return 0

    #Check Next Item
    else:
        return find(data[1:], value) + 1

print(find(["hi", "there", "you", "there"], "there"))
print(find(["hi", "henry", "you", "there"], "there"))
print(find([10, 20, 30], 0))