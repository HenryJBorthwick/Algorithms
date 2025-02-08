import sys
sys.setrecursionlimit(100000)

def dumbo_func(data, index=0):
    """Takes a list of numbers and does weird stuff with it"""
    if len(data) == index:
        return 0
    else:
        if (data[index] // 100) % 3 != 0:
            return 1 + dumbo_func(data, index+1)
        else:
            return dumbo_func(data, index+1)
        
# Simple test with short list.
# Original func works fine on this
data = [677, 90, 785, 875, 7, 90393, 10707]
print(dumbo_func(data))